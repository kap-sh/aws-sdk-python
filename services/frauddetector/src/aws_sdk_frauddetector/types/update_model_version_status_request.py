"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateModelVersionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float_version_string
    import aws_sdk_frauddetector.types.model_identifier
    import aws_sdk_frauddetector.types.model_type_enum
    import aws_sdk_frauddetector.types.model_version_status


class UpdateModelVersionStatusRequest(TypedDict, closed=True):
    model_id: "aws_sdk_frauddetector.types.model_identifier.modelIdentifier"
    """<p>The model ID of the model version to update.</p>"""
    model_type: "aws_sdk_frauddetector.types.model_type_enum.ModelTypeEnum"
    """<p>The model type.</p>"""
    model_version_number: (
        "aws_sdk_frauddetector.types.float_version_string.floatVersionString"
    )
    """<p>The model version number.</p>"""
    status: "aws_sdk_frauddetector.types.model_version_status.ModelVersionStatus"
    """<p>The model version status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateModelVersionStatusRequest) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import aws_sdk_frauddetector.types.model_type_enum

    out["modelType"] = (
        aws_sdk_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
            value["model_type"]
        )
    )
    out["modelVersionNumber"] = value["model_version_number"]
    import aws_sdk_frauddetector.types.model_version_status

    out["status"] = (
        aws_sdk_frauddetector.types.model_version_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateModelVersionStatusRequest:
    out: UpdateModelVersionStatusRequest = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("UpdateModelVersionStatusRequest.model_id required")
    if "modelType" in data:
        import aws_sdk_frauddetector.types.model_type_enum

        out["model_type"] = (
            aws_sdk_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateModelVersionStatusRequest.model_type required"
        )
    if "modelVersionNumber" in data:
        out["model_version_number"] = data["modelVersionNumber"]
    else:
        raise DeserializationError(
            "UpdateModelVersionStatusRequest.model_version_number required"
        )
    if "status" in data:
        import aws_sdk_frauddetector.types.model_version_status

        out["status"] = (
            aws_sdk_frauddetector.types.model_version_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateModelVersionStatusRequest.status required")
    return out
