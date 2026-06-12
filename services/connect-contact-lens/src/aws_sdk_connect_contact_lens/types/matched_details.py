"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#MatchedDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect_contact_lens.types.category_details
    import aws_sdk_connect_contact_lens.types.category_name

MatchedDetails: TypeAlias = dict[
    "aws_sdk_connect_contact_lens.types.category_name.CategoryName",
    "aws_sdk_connect_contact_lens.types.category_details.CategoryDetails",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MatchedDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_connect_contact_lens.types.category_details

        out[key] = aws_sdk_connect_contact_lens.types.category_details.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> MatchedDetails:
    out: MatchedDetails = {}
    for key, value in data.items():
        import aws_sdk_connect_contact_lens.types.category_details

        out[key] = aws_sdk_connect_contact_lens.types.category_details.deserialize_json(
            value
        )
    return out
