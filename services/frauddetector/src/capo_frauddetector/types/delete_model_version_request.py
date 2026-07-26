"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteModelVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.float_version_string
    import capo_frauddetector.types.model_identifier
    import capo_frauddetector.types.model_type_enum


class DeleteModelVersionRequest(TypedDict, closed=True):
    model_id: "capo_frauddetector.types.model_identifier.modelIdentifier"
    """<p>The model ID of the model version to delete.</p>"""
    model_type: "capo_frauddetector.types.model_type_enum.ModelTypeEnum"
    """<p>The model type of the model version to delete.</p>"""
    model_version_number: (
        "capo_frauddetector.types.float_version_string.floatVersionString"
    )
    """<p>The model version number of the model version to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteModelVersionRequest) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import capo_frauddetector.types.model_type_enum

    out["modelType"] = capo_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
        value["model_type"]
    )
    out["modelVersionNumber"] = value["model_version_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteModelVersionRequest:
    out: DeleteModelVersionRequest = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("DeleteModelVersionRequest.model_id required")
    if "modelType" in data:
        import capo_frauddetector.types.model_type_enum

        out["model_type"] = (
            capo_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    else:
        raise DeserializationError("DeleteModelVersionRequest.model_type required")
    if "modelVersionNumber" in data:
        out["model_version_number"] = data["modelVersionNumber"]
    else:
        raise DeserializationError(
            "DeleteModelVersionRequest.model_version_number required"
        )
    return out
