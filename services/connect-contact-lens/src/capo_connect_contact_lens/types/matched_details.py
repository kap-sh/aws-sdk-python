"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#MatchedDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.category_details
    import capo_connect_contact_lens.types.category_name

MatchedDetails: TypeAlias = dict[
    "capo_connect_contact_lens.types.category_name.CategoryName",
    "capo_connect_contact_lens.types.category_details.CategoryDetails",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MatchedDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_connect_contact_lens.types.category_details

        out[key] = capo_connect_contact_lens.types.category_details.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> MatchedDetails:
    out: MatchedDetails = {}
    for key, value in data.items():
        import capo_connect_contact_lens.types.category_details

        out[key] = capo_connect_contact_lens.types.category_details.deserialize_json(
            value
        )
    return out
