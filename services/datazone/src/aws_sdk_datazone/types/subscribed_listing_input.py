"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedListingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.listing_id


class SubscribedListingInput(TypedDict, closed=True):
    identifier: "aws_sdk_datazone.types.listing_id.ListingId"
    """<p>The identifier of the published asset for which the subscription grant is to be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedListingInput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> SubscribedListingInput:
    out: SubscribedListingInput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("SubscribedListingInput.identifier required")
    return out
