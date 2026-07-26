"""Generated from Smithy shape ``com.amazonaws.bedrock#InvocationLogSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.s3_uri


class _InvocationLogSource_s3Uri(TypedDict, closed=True):
    s3Uri: "capo_bedrock.types.s3_uri.S3Uri"


InvocationLogSource: TypeAlias = _InvocationLogSource_s3Uri


# --- restJson1 ser/de ---
def serialize_json(value: InvocationLogSource) -> dict:
    if "s3Uri" in value:
        return {"s3Uri": value["s3Uri"]}
    else:
        raise SerializationError("InvocationLogSource: no variant present")


def deserialize_json(data: dict) -> InvocationLogSource:
    if "s3Uri" in data:
        return {"s3Uri": data["s3Uri"]}
    else:
        raise DeserializationError("InvocationLogSource: no recognized variant key")
