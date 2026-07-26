"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetMLModelTrainingJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.ml_models
    import capo_neptunedata.types.ml_resource_definition


class GetMLModelTrainingJobOutput(TypedDict, closed=True):
    status: NotRequired["str"]
    """<p>The status of the model training job.</p>"""
    id: NotRequired["str"]
    """<p>The unique identifier of this model-training job.</p>"""
    processing_job: NotRequired[
        "capo_neptunedata.types.ml_resource_definition.MlResourceDefinition"
    ]
    """<p>The data processing job.</p>"""
    hpo_job: NotRequired[
        "capo_neptunedata.types.ml_resource_definition.MlResourceDefinition"
    ]
    """<p>The HPO job.</p>"""
    model_transform_job: NotRequired[
        "capo_neptunedata.types.ml_resource_definition.MlResourceDefinition"
    ]
    """<p>The model transform job.</p>"""
    ml_models: NotRequired["capo_neptunedata.types.ml_models.MlModels"]
    """<p>A list of the configurations of the ML models being used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMLModelTrainingJobOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "id" in value:
        out["id"] = value["id"]
    if "processing_job" in value:
        import capo_neptunedata.types.ml_resource_definition

        out["processingJob"] = (
            capo_neptunedata.types.ml_resource_definition.serialize_json(
                value["processing_job"]
            )
        )
    if "hpo_job" in value:
        import capo_neptunedata.types.ml_resource_definition

        out["hpoJob"] = capo_neptunedata.types.ml_resource_definition.serialize_json(
            value["hpo_job"]
        )
    if "model_transform_job" in value:
        import capo_neptunedata.types.ml_resource_definition

        out["modelTransformJob"] = (
            capo_neptunedata.types.ml_resource_definition.serialize_json(
                value["model_transform_job"]
            )
        )
    if "ml_models" in value:
        import capo_neptunedata.types.ml_models

        out["mlModels"] = capo_neptunedata.types.ml_models.serialize_json(
            value["ml_models"]
        )
    return out


def deserialize_json(data: dict) -> GetMLModelTrainingJobOutput:
    out: GetMLModelTrainingJobOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "id" in data:
        out["id"] = data["id"]
    if "processingJob" in data:
        import capo_neptunedata.types.ml_resource_definition

        out["processing_job"] = (
            capo_neptunedata.types.ml_resource_definition.deserialize_json(
                data["processingJob"]
            )
        )
    if "hpoJob" in data:
        import capo_neptunedata.types.ml_resource_definition

        out["hpo_job"] = capo_neptunedata.types.ml_resource_definition.deserialize_json(
            data["hpoJob"]
        )
    if "modelTransformJob" in data:
        import capo_neptunedata.types.ml_resource_definition

        out["model_transform_job"] = (
            capo_neptunedata.types.ml_resource_definition.deserialize_json(
                data["modelTransformJob"]
            )
        )
    if "mlModels" in data:
        import capo_neptunedata.types.ml_models

        out["ml_models"] = capo_neptunedata.types.ml_models.deserialize_json(
            data["mlModels"]
        )
    return out
