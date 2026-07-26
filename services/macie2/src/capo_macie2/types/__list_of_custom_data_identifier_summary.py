"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfCustomDataIdentifierSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.custom_data_identifier_summary

__listOfCustomDataIdentifierSummary: TypeAlias = list[
    "capo_macie2.types.custom_data_identifier_summary.CustomDataIdentifierSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCustomDataIdentifierSummary) -> list:
    import capo_macie2.types.custom_data_identifier_summary

    out: list = []
    for item in value:
        out.append(
            capo_macie2.types.custom_data_identifier_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfCustomDataIdentifierSummary:
    import capo_macie2.types.custom_data_identifier_summary

    out: __listOfCustomDataIdentifierSummary = []
    for item in data:
        out.append(
            capo_macie2.types.custom_data_identifier_summary.deserialize_json(item)
        )
    return out
