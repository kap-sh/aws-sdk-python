"""Generated from Smithy shape ``com.amazonaws.quicksight#ListThemeVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.theme_version_summary_list


class ListThemeVersionsResponse(TypedDict, closed=True):
    theme_version_summary_list: NotRequired[
        "aws_sdk_quicksight.types.theme_version_summary_list.ThemeVersionSummaryList"
    ]
    """<p>A structure containing a list of all the versions of the specified theme.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThemeVersionsResponse) -> dict:
    out: dict = {}
    if "theme_version_summary_list" in value:
        import aws_sdk_quicksight.types.theme_version_summary_list

        out["ThemeVersionSummaryList"] = (
            aws_sdk_quicksight.types.theme_version_summary_list.serialize_json(
                value["theme_version_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListThemeVersionsResponse:
    out: ListThemeVersionsResponse = {}  # type: ignore[typeddict-item]
    if "ThemeVersionSummaryList" in data:
        import aws_sdk_quicksight.types.theme_version_summary_list

        out["theme_version_summary_list"] = (
            aws_sdk_quicksight.types.theme_version_summary_list.deserialize_json(
                data["ThemeVersionSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
