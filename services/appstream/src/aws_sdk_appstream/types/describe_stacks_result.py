"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeStacksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.stack_list
    import aws_sdk_appstream.types.string


class DescribeStacksResult(TypedDict, closed=True):
    stacks: NotRequired["aws_sdk_appstream.types.stack_list.StackList"]
    """<p>Information about the stacks.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStacksResult) -> dict:
    out: dict = {}
    if "stacks" in value:
        import aws_sdk_appstream.types.stack_list

        out["Stacks"] = aws_sdk_appstream.types.stack_list.serialize_aws_json_1_1(
            value["stacks"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStacksResult:
    out: DescribeStacksResult = {}  # type: ignore[typeddict-item]
    if "Stacks" in data:
        import aws_sdk_appstream.types.stack_list

        out["stacks"] = aws_sdk_appstream.types.stack_list.deserialize_aws_json_1_1(
            data["Stacks"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
