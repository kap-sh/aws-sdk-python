"""Generated from Smithy shape ``com.amazonaws.macie2#BatchGetCustomDataIdentifiersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of__string
    import aws_sdk_macie2.types.__list_of_batch_get_custom_data_identifier_summary


class BatchGetCustomDataIdentifiersResponse(TypedDict):
    custom_data_identifiers: NotRequired[
        "aws_sdk_macie2.types.__list_of_batch_get_custom_data_identifier_summary.__listOfBatchGetCustomDataIdentifierSummary"
    ]
    """<p>An array of objects, one for each custom data identifier that matches the criteria specified in the request.</p>"""
    not_found_identifier_ids: NotRequired[
        "aws_sdk_macie2.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of custom data identifier IDs, one for each custom data identifier that was specified in the request but doesn't correlate to an existing custom data identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCustomDataIdentifiersResponse) -> dict:
    out: dict = {}
    if "custom_data_identifiers" in value:
        import aws_sdk_macie2.types.__list_of_batch_get_custom_data_identifier_summary

        out["customDataIdentifiers"] = (
            aws_sdk_macie2.types.__list_of_batch_get_custom_data_identifier_summary.serialize_json(
                value["custom_data_identifiers"]
            )
        )
    if "not_found_identifier_ids" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["notFoundIdentifierIds"] = (
            aws_sdk_macie2.types.__list_of__string.serialize_json(
                value["not_found_identifier_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetCustomDataIdentifiersResponse:
    out: BatchGetCustomDataIdentifiersResponse = {}  # type: ignore[typeddict-item]
    if "customDataIdentifiers" in data:
        import aws_sdk_macie2.types.__list_of_batch_get_custom_data_identifier_summary

        out["custom_data_identifiers"] = (
            aws_sdk_macie2.types.__list_of_batch_get_custom_data_identifier_summary.deserialize_json(
                data["customDataIdentifiers"]
            )
        )
    if "notFoundIdentifierIds" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["not_found_identifier_ids"] = (
            aws_sdk_macie2.types.__list_of__string.deserialize_json(
                data["notFoundIdentifierIds"]
            )
        )
    return out
