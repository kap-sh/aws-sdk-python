"""Generated from Smithy shape ``com.amazonaws.datazone#Permissions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.s3_permissions


class _Permissions_s3(TypedDict, closed=True):
    s3: "capo_datazone.types.s3_permissions.S3Permissions"


Permissions: TypeAlias = _Permissions_s3


# --- restJson1 ser/de ---
def serialize_json(value: Permissions) -> dict:
    if "s3" in value:
        import capo_datazone.types.s3_permissions

        return {"s3": capo_datazone.types.s3_permissions.serialize_json(value["s3"])}
    else:
        raise SerializationError("Permissions: no variant present")


def deserialize_json(data: dict) -> Permissions:
    if "s3" in data:
        import capo_datazone.types.s3_permissions

        return {"s3": capo_datazone.types.s3_permissions.deserialize_json(data["s3"])}
    else:
        raise DeserializationError("Permissions: no recognized variant key")
