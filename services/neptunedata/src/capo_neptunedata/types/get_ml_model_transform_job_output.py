"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetMLModelTransformJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.ml_resource_definition
    import capo_neptunedata.types.models


class GetMLModelTransformJobOutput(TypedDict, closed=True):
    status: NotRequired["str"]
    """<p>The status of the model-transform job.</p>"""
    id: NotRequired["str"]
    """<p>The unique identifier of the model-transform job to be retrieved.</p>"""
    base_processing_job: NotRequired[
        "capo_neptunedata.types.ml_resource_definition.MlResourceDefinition"
    ]
    """<p>The base data processing job.</p>"""
    remote_model_transform_job: NotRequired[
        "capo_neptunedata.types.ml_resource_definition.MlResourceDefinition"
    ]
    """<p>The remote model transform job.</p>"""
    models: NotRequired["capo_neptunedata.types.models.Models"]
    """<p>A list of the configuration information for the models being used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMLModelTransformJobOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "id" in value:
        out["id"] = value["id"]
    if "base_processing_job" in value:
        import capo_neptunedata.types.ml_resource_definition

        out["baseProcessingJob"] = (
            capo_neptunedata.types.ml_resource_definition.serialize_json(
                value["base_processing_job"]
            )
        )
    if "remote_model_transform_job" in value:
        import capo_neptunedata.types.ml_resource_definition

        out["remoteModelTransformJob"] = (
            capo_neptunedata.types.ml_resource_definition.serialize_json(
                value["remote_model_transform_job"]
            )
        )
    if "models" in value:
        import capo_neptunedata.types.models

        out["models"] = capo_neptunedata.types.models.serialize_json(value["models"])
    return out


def deserialize_json(data: dict) -> GetMLModelTransformJobOutput:
    out: GetMLModelTransformJobOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "id" in data:
        out["id"] = data["id"]
    if "baseProcessingJob" in data:
        import capo_neptunedata.types.ml_resource_definition

        out["base_processing_job"] = (
            capo_neptunedata.types.ml_resource_definition.deserialize_json(
                data["baseProcessingJob"]
            )
        )
    if "remoteModelTransformJob" in data:
        import capo_neptunedata.types.ml_resource_definition

        out["remote_model_transform_job"] = (
            capo_neptunedata.types.ml_resource_definition.deserialize_json(
                data["remoteModelTransformJob"]
            )
        )
    if "models" in data:
        import capo_neptunedata.types.models

        out["models"] = capo_neptunedata.types.models.deserialize_json(data["models"])
    return out
