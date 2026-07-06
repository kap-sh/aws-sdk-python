"""Generated from Smithy shape ``com.amazonaws.codebuild#ListBuildsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.sort_order_type
    import aws_sdk_codebuild.types.string


class ListBuildsInput(TypedDict, closed=True):
    sort_order: NotRequired["aws_sdk_codebuild.types.sort_order_type.SortOrderType"]
    """<p>The order to list build IDs. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List the build IDs in ascending order by build ID.</p> </li> <li> <p> <code>DESCENDING</code>: List the build IDs in descending order by build ID.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBuildsInput) -> dict:
    out: dict = {}
    if "sort_order" in value:
        import aws_sdk_codebuild.types.sort_order_type

        out["sortOrder"] = (
            aws_sdk_codebuild.types.sort_order_type.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBuildsInput:
    out: ListBuildsInput = {}  # type: ignore[typeddict-item]
    if "sortOrder" in data:
        import aws_sdk_codebuild.types.sort_order_type

        out["sort_order"] = (
            aws_sdk_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
