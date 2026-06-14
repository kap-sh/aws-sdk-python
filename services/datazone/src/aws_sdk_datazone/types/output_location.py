"""Generated from Smithy shape ``com.amazonaws.datazone#OutputLocation``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.s3_destination


class _OutputLocation_s3(TypedDict):
    s3: "aws_sdk_datazone.types.s3_destination.S3Destination"


OutputLocation: TypeAlias = _OutputLocation_s3


# --- restJson1 ser/de ---
def serialize_json(value: OutputLocation) -> dict:
    if "s3" in value:
        import aws_sdk_datazone.types.s3_destination

        return {"s3": aws_sdk_datazone.types.s3_destination.serialize_json(value["s3"])}
    else:
        raise SerializationError("OutputLocation: no variant present")


def deserialize_json(data: dict) -> OutputLocation:
    if "s3" in data:
        import aws_sdk_datazone.types.s3_destination

        return {
            "s3": aws_sdk_datazone.types.s3_destination.deserialize_json(data["s3"])
        }
    else:
        raise DeserializationError("OutputLocation: no recognized variant key")
