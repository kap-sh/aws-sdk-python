"""Generated from Smithy shape ``com.amazonaws.datazone#Permissions``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.s3_permissions


class _Permissions_s3(TypedDict):
    s3: "aws_sdk_datazone.types.s3_permissions.S3Permissions"


Permissions: TypeAlias = _Permissions_s3


# --- restJson1 ser/de ---
def serialize_json(value: Permissions) -> dict:
    if "s3" in value:
        import aws_sdk_datazone.types.s3_permissions

        return {"s3": aws_sdk_datazone.types.s3_permissions.serialize_json(value["s3"])}
    else:
        raise SerializationError("Permissions: no variant present")


def deserialize_json(data: dict) -> Permissions:
    if "s3" in data:
        import aws_sdk_datazone.types.s3_permissions

        return {
            "s3": aws_sdk_datazone.types.s3_permissions.deserialize_json(data["s3"])
        }
    else:
        raise DeserializationError("Permissions: no recognized variant key")
