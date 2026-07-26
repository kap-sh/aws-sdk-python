"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfManagedDataIdentifierSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.managed_data_identifier_summary

__listOfManagedDataIdentifierSummary: TypeAlias = list[
    "capo_macie2.types.managed_data_identifier_summary.ManagedDataIdentifierSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfManagedDataIdentifierSummary) -> list:
    import capo_macie2.types.managed_data_identifier_summary

    out: list = []
    for item in value:
        out.append(
            capo_macie2.types.managed_data_identifier_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfManagedDataIdentifierSummary:
    import capo_macie2.types.managed_data_identifier_summary

    out: __listOfManagedDataIdentifierSummary = []
    for item in data:
        out.append(
            capo_macie2.types.managed_data_identifier_summary.deserialize_json(item)
        )
    return out
