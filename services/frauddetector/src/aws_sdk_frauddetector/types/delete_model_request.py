"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.model_identifier
    import aws_sdk_frauddetector.types.model_type_enum


class DeleteModelRequest(TypedDict):
    model_id: "aws_sdk_frauddetector.types.model_identifier.modelIdentifier"
    """<p>The model ID of the model to delete.</p>"""
    model_type: "aws_sdk_frauddetector.types.model_type_enum.ModelTypeEnum"
    """<p>The model type of the model to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteModelRequest) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import aws_sdk_frauddetector.types.model_type_enum

    out["modelType"] = (
        aws_sdk_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
            value["model_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteModelRequest:
    out: DeleteModelRequest = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("DeleteModelRequest.model_id required")
    if "modelType" in data:
        import aws_sdk_frauddetector.types.model_type_enum

        out["model_type"] = (
            aws_sdk_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    else:
        raise DeserializationError("DeleteModelRequest.model_type required")
    return out
