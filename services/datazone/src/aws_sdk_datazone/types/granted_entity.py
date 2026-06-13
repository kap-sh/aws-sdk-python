"""Generated from Smithy shape ``com.amazonaws.datazone#GrantedEntity``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.listing_revision


class _GrantedEntity_listing(TypedDict):
    listing: "aws_sdk_datazone.types.listing_revision.ListingRevision"


GrantedEntity: TypeAlias = _GrantedEntity_listing


# --- restJson1 ser/de ---
def serialize_json(value: GrantedEntity) -> dict:
    if "listing" in value:
        import aws_sdk_datazone.types.listing_revision

        return {
            "listing": aws_sdk_datazone.types.listing_revision.serialize_json(
                value["listing"]
            )
        }
    else:
        raise SerializationError("GrantedEntity: no variant present")


def deserialize_json(data: dict) -> GrantedEntity:
    if "listing" in data:
        import aws_sdk_datazone.types.listing_revision

        return {
            "listing": aws_sdk_datazone.types.listing_revision.deserialize_json(
                data["listing"]
            )
        }
    else:
        raise DeserializationError("GrantedEntity: no recognized variant key")
