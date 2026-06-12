"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeAppBlocksResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.app_blocks
    import aws_sdk_appstream.types.string


class DescribeAppBlocksResult(TypedDict):
    app_blocks: NotRequired["aws_sdk_appstream.types.app_blocks.AppBlocks"]
    """<p>The app blocks in the list.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAppBlocksResult) -> dict:
    out: dict = {}
    if "app_blocks" in value:
        import aws_sdk_appstream.types.app_blocks

        out["AppBlocks"] = aws_sdk_appstream.types.app_blocks.serialize_aws_json_1_1(
            value["app_blocks"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAppBlocksResult:
    out: DescribeAppBlocksResult = {}  # type: ignore[typeddict-item]
    if "AppBlocks" in data:
        import aws_sdk_appstream.types.app_blocks

        out["app_blocks"] = aws_sdk_appstream.types.app_blocks.deserialize_aws_json_1_1(
            data["AppBlocks"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
