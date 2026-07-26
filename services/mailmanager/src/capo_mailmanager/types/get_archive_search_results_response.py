"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveSearchResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.rows_list


class GetArchiveSearchResultsResponse(TypedDict, closed=True):
    rows: NotRequired["capo_mailmanager.types.rows_list.RowsList"]
    """<p>The list of email result objects matching the search criteria.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveSearchResultsResponse) -> dict:
    out: dict = {}
    if "rows" in value:
        import capo_mailmanager.types.rows_list

        out["Rows"] = capo_mailmanager.types.rows_list.serialize_aws_json_1_0(
            value["rows"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveSearchResultsResponse:
    out: GetArchiveSearchResultsResponse = {}  # type: ignore[typeddict-item]
    if "Rows" in data:
        import capo_mailmanager.types.rows_list

        out["rows"] = capo_mailmanager.types.rows_list.deserialize_aws_json_1_0(
            data["Rows"]
        )
    return out
