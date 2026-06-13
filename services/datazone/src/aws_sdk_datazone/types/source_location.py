"""Generated from Smithy shape ``com.amazonaws.datazone#SourceLocation``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.s3_source_location


class _SourceLocation_s3(TypedDict):
    s3: "aws_sdk_datazone.types.s3_source_location.S3SourceLocation"


SourceLocation: TypeAlias = _SourceLocation_s3


# --- restJson1 ser/de ---
def serialize_json(value: SourceLocation) -> dict:
    if "s3" in value:
        return {"s3": value["s3"]}
    else:
        raise SerializationError("SourceLocation: no variant present")


def deserialize_json(data: dict) -> SourceLocation:
    if "s3" in data:
        return {"s3": data["s3"]}
    else:
        raise DeserializationError("SourceLocation: no recognized variant key")
