"""Generated from Smithy shape ``com.amazonaws.macie2#ListManagedDataIdentifiersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_managed_data_identifier_summary
    import capo_macie2.types.__string


class ListManagedDataIdentifiersResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_macie2.types.__list_of_managed_data_identifier_summary.__listOfManagedDataIdentifierSummary"
    ]
    """<p>An array of objects, one for each managed data identifier.</p>"""
    next_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedDataIdentifiersResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_macie2.types.__list_of_managed_data_identifier_summary

        out["items"] = (
            capo_macie2.types.__list_of_managed_data_identifier_summary.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListManagedDataIdentifiersResponse:
    out: ListManagedDataIdentifiersResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_macie2.types.__list_of_managed_data_identifier_summary

        out["items"] = (
            capo_macie2.types.__list_of_managed_data_identifier_summary.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
