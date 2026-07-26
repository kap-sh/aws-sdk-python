"""Generated from Smithy shape ``com.amazonaws.macie2#BatchGetCustomDataIdentifiersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of__string
    import capo_macie2.types.__list_of_batch_get_custom_data_identifier_summary


class BatchGetCustomDataIdentifiersResponse(TypedDict, closed=True):
    custom_data_identifiers: NotRequired[
        "capo_macie2.types.__list_of_batch_get_custom_data_identifier_summary.__listOfBatchGetCustomDataIdentifierSummary"
    ]
    """<p>An array of objects, one for each custom data identifier that matches the criteria specified in the request.</p>"""
    not_found_identifier_ids: NotRequired[
        "capo_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of custom data identifier IDs, one for each custom data identifier that was specified in the request but doesn't correlate to an existing custom data identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCustomDataIdentifiersResponse) -> dict:
    out: dict = {}
    if "custom_data_identifiers" in value:
        import capo_macie2.types.__list_of_batch_get_custom_data_identifier_summary

        out["customDataIdentifiers"] = (
            capo_macie2.types.__list_of_batch_get_custom_data_identifier_summary.serialize_json(
                value["custom_data_identifiers"]
            )
        )
    if "not_found_identifier_ids" in value:
        import capo_macie2.types.__list_of__string

        out["notFoundIdentifierIds"] = (
            capo_macie2.types.__list_of__string.serialize_json(
                value["not_found_identifier_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetCustomDataIdentifiersResponse:
    out: BatchGetCustomDataIdentifiersResponse = {}  # type: ignore[typeddict-item]
    if "customDataIdentifiers" in data:
        import capo_macie2.types.__list_of_batch_get_custom_data_identifier_summary

        out["custom_data_identifiers"] = (
            capo_macie2.types.__list_of_batch_get_custom_data_identifier_summary.deserialize_json(
                data["customDataIdentifiers"]
            )
        )
    if "notFoundIdentifierIds" in data:
        import capo_macie2.types.__list_of__string

        out["not_found_identifier_ids"] = (
            capo_macie2.types.__list_of__string.deserialize_json(
                data["notFoundIdentifierIds"]
            )
        )
    return out
