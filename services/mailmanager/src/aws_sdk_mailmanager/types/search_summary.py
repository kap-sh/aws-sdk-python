"""Generated from Smithy shape ``com.amazonaws.mailmanager#SearchSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.search_id
    import aws_sdk_mailmanager.types.search_status


class SearchSummary(TypedDict):
    search_id: NotRequired["aws_sdk_mailmanager.types.search_id.SearchId"]
    """<p>The unique identifier of the search job.</p>"""
    status: NotRequired["aws_sdk_mailmanager.types.search_status.SearchStatus"]
    """<p>The current status of the search job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchSummary) -> dict:
    out: dict = {}
    if "search_id" in value:
        out["SearchId"] = value["search_id"]
    if "status" in value:
        import aws_sdk_mailmanager.types.search_status

        out["Status"] = aws_sdk_mailmanager.types.search_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchSummary:
    out: SearchSummary = {}  # type: ignore[typeddict-item]
    if "SearchId" in data:
        out["search_id"] = data["SearchId"]
    if "Status" in data:
        import aws_sdk_mailmanager.types.search_status

        out["status"] = (
            aws_sdk_mailmanager.types.search_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
