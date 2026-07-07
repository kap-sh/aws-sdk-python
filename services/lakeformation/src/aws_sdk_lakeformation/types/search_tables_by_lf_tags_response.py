"""Generated from Smithy shape ``com.amazonaws.lakeformation#SearchTablesByLFTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.table_lf_tags_list
    import aws_sdk_lakeformation.types.token


class SearchTablesByLFTagsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_lakeformation.types.token.Token"]
    """<p>A continuation token, present if the current list segment is not the last. On the first run, if you include a not null (a value) token you can get empty pages.</p>"""
    table_list: NotRequired[
        "aws_sdk_lakeformation.types.table_lf_tags_list.TableLFTagsList"
    ]
    """<p>A list of tables that meet the LF-tag conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchTablesByLFTagsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "table_list" in value:
        import aws_sdk_lakeformation.types.table_lf_tags_list

        out["TableList"] = (
            aws_sdk_lakeformation.types.table_lf_tags_list.serialize_json(
                value["table_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchTablesByLFTagsResponse:
    out: SearchTablesByLFTagsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TableList" in data:
        import aws_sdk_lakeformation.types.table_lf_tags_list

        out["table_list"] = (
            aws_sdk_lakeformation.types.table_lf_tags_list.deserialize_json(
                data["TableList"]
            )
        )
    return out
