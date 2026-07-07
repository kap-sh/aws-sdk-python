"""Generated from Smithy shape ``com.amazonaws.m2#ExternalLocation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_m2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.string2000


class _ExternalLocation_s3Location(TypedDict, closed=True):
    s3Location: "aws_sdk_m2.types.string2000.String2000"


ExternalLocation: TypeAlias = _ExternalLocation_s3Location


# --- restJson1 ser/de ---
def serialize_json(value: ExternalLocation) -> dict:
    if "s3Location" in value:
        return {"s3Location": value["s3Location"]}
    else:
        raise SerializationError("ExternalLocation: no variant present")


def deserialize_json(data: dict) -> ExternalLocation:
    if "s3Location" in data:
        return {"s3Location": data["s3Location"]}
    else:
        raise DeserializationError("ExternalLocation: no recognized variant key")
