"""Generated from Smithy shape ``com.amazonaws.quicksight#ListThemeAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.theme_alias_list


class ListThemeAliasesResponse(TypedDict, closed=True):
    theme_alias_list: NotRequired[
        "aws_sdk_quicksight.types.theme_alias_list.ThemeAliasList"
    ]
    """<p>A structure containing the list of the theme's aliases.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThemeAliasesResponse) -> dict:
    out: dict = {}
    if "theme_alias_list" in value:
        import aws_sdk_quicksight.types.theme_alias_list

        out["ThemeAliasList"] = (
            aws_sdk_quicksight.types.theme_alias_list.serialize_json(
                value["theme_alias_list"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThemeAliasesResponse:
    out: ListThemeAliasesResponse = {}  # type: ignore[typeddict-item]
    if "ThemeAliasList" in data:
        import aws_sdk_quicksight.types.theme_alias_list

        out["theme_alias_list"] = (
            aws_sdk_quicksight.types.theme_alias_list.deserialize_json(
                data["ThemeAliasList"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
