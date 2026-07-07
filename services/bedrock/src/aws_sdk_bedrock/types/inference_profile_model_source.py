"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceProfileModelSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.inference_profile_model_source_arn


class _InferenceProfileModelSource_copyFrom(TypedDict, closed=True):
    copyFrom: "aws_sdk_bedrock.types.inference_profile_model_source_arn.InferenceProfileModelSourceArn"


InferenceProfileModelSource: TypeAlias = _InferenceProfileModelSource_copyFrom


# --- restJson1 ser/de ---
def serialize_json(value: InferenceProfileModelSource) -> dict:
    if "copyFrom" in value:
        return {"copyFrom": value["copyFrom"]}
    else:
        raise SerializationError("InferenceProfileModelSource: no variant present")


def deserialize_json(data: dict) -> InferenceProfileModelSource:
    if "copyFrom" in data:
        return {"copyFrom": data["copyFrom"]}
    else:
        raise DeserializationError(
            "InferenceProfileModelSource: no recognized variant key"
        )
