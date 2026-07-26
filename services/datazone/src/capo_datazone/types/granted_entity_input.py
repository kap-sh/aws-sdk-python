"""Generated from Smithy shape ``com.amazonaws.datazone#GrantedEntityInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.listing_revision_input


class _GrantedEntityInput_listing(TypedDict, closed=True):
    listing: "capo_datazone.types.listing_revision_input.ListingRevisionInput"


GrantedEntityInput: TypeAlias = _GrantedEntityInput_listing


# --- restJson1 ser/de ---
def serialize_json(value: GrantedEntityInput) -> dict:
    if "listing" in value:
        import capo_datazone.types.listing_revision_input

        return {
            "listing": capo_datazone.types.listing_revision_input.serialize_json(
                value["listing"]
            )
        }
    else:
        raise SerializationError("GrantedEntityInput: no variant present")


def deserialize_json(data: dict) -> GrantedEntityInput:
    if "listing" in data:
        import capo_datazone.types.listing_revision_input

        return {
            "listing": capo_datazone.types.listing_revision_input.deserialize_json(
                data["listing"]
            )
        }
    else:
        raise DeserializationError("GrantedEntityInput: no recognized variant key")
