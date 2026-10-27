
from pycaret.classification import setup, compare_models, finalize_model
from pycaret.datasets import get_data
from pycaret.classification import save_model

iris = get_data('iris')

setup(
    data=iris,
    target='species',
    session_id=42,
    verbose=False,
    html=False,
    log_experiment=False
)

model = compare_models()
final_model = finalize_model(model)

save_model(final_model, 'iris_model')
print("Model retraining completed")
