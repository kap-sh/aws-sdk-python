"""Generated from Smithy shape ``com.amazonaws.macie2#ListFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of__string
    import capo_macie2.types.__string


class ListFindingsResponse(TypedDict, closed=True):
    finding_ids: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array of strings, where each string is the unique identifier for a finding that matches the filter criteria specified in the request.</p>"""
    next_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsResponse) -> dict:
    out: dict = {}
    if "finding_ids" in value:
        import capo_macie2.types.__list_of__string

        out["findingIds"] = capo_macie2.types.__list_of__string.serialize_json(
            value["finding_ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingsResponse:
    out: ListFindingsResponse = {}  # type: ignore[typeddict-item]
    if "findingIds" in data:
        import capo_macie2.types.__list_of__string

        out["finding_ids"] = capo_macie2.types.__list_of__string.deserialize_json(
            data["findingIds"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
