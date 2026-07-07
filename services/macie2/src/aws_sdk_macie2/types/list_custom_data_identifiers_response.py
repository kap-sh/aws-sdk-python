"""Generated from Smithy shape ``com.amazonaws.macie2#ListCustomDataIdentifiersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_custom_data_identifier_summary
    import aws_sdk_macie2.types.__string


class ListCustomDataIdentifiersResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_macie2.types.__list_of_custom_data_identifier_summary.__listOfCustomDataIdentifierSummary"
    ]
    """<p>An array of objects, one for each custom data identifier.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomDataIdentifiersResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_macie2.types.__list_of_custom_data_identifier_summary

        out["items"] = (
            aws_sdk_macie2.types.__list_of_custom_data_identifier_summary.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomDataIdentifiersResponse:
    out: ListCustomDataIdentifiersResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_macie2.types.__list_of_custom_data_identifier_summary

        out["items"] = (
            aws_sdk_macie2.types.__list_of_custom_data_identifier_summary.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
