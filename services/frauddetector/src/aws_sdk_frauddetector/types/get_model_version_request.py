"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetModelVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float_version_string
    import aws_sdk_frauddetector.types.model_identifier
    import aws_sdk_frauddetector.types.model_type_enum


class GetModelVersionRequest(TypedDict):
    model_id: "aws_sdk_frauddetector.types.model_identifier.modelIdentifier"
    """<p>The model ID.</p>"""
    model_type: "aws_sdk_frauddetector.types.model_type_enum.ModelTypeEnum"
    """<p>The model type.</p>"""
    model_version_number: (
        "aws_sdk_frauddetector.types.float_version_string.floatVersionString"
    )
    """<p>The model version number.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetModelVersionRequest) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import aws_sdk_frauddetector.types.model_type_enum

    out["modelType"] = (
        aws_sdk_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
            value["model_type"]
        )
    )
    out["modelVersionNumber"] = value["model_version_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetModelVersionRequest:
    out: GetModelVersionRequest = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("GetModelVersionRequest.model_id required")
    if "modelType" in data:
        import aws_sdk_frauddetector.types.model_type_enum

        out["model_type"] = (
            aws_sdk_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    else:
        raise DeserializationError("GetModelVersionRequest.model_type required")
    if "modelVersionNumber" in data:
        out["model_version_number"] = data["modelVersionNumber"]
    else:
        raise DeserializationError(
            "GetModelVersionRequest.model_version_number required"
        )
    return out
