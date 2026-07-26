"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfBatchGetCustomDataIdentifierSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.batch_get_custom_data_identifier_summary

__listOfBatchGetCustomDataIdentifierSummary: TypeAlias = list[
    "capo_macie2.types.batch_get_custom_data_identifier_summary.BatchGetCustomDataIdentifierSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBatchGetCustomDataIdentifierSummary) -> list:
    import capo_macie2.types.batch_get_custom_data_identifier_summary

    out: list = []
    for item in value:
        out.append(
            capo_macie2.types.batch_get_custom_data_identifier_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfBatchGetCustomDataIdentifierSummary:
    import capo_macie2.types.batch_get_custom_data_identifier_summary

    out: __listOfBatchGetCustomDataIdentifierSummary = []
    for item in data:
        out.append(
            capo_macie2.types.batch_get_custom_data_identifier_summary.deserialize_json(
                item
            )
        )
    return out
