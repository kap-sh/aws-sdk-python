"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeAppBlockBuildersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.app_block_builder_list
    import aws_sdk_appstream.types.string


class DescribeAppBlockBuildersResult(TypedDict, closed=True):
    app_block_builders: NotRequired[
        "aws_sdk_appstream.types.app_block_builder_list.AppBlockBuilderList"
    ]
    """<p>The list that describes one or more app block builders.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAppBlockBuildersResult) -> dict:
    out: dict = {}
    if "app_block_builders" in value:
        import aws_sdk_appstream.types.app_block_builder_list

        out["AppBlockBuilders"] = (
            aws_sdk_appstream.types.app_block_builder_list.serialize_aws_json_1_1(
                value["app_block_builders"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAppBlockBuildersResult:
    out: DescribeAppBlockBuildersResult = {}  # type: ignore[typeddict-item]
    if "AppBlockBuilders" in data:
        import aws_sdk_appstream.types.app_block_builder_list

        out["app_block_builders"] = (
            aws_sdk_appstream.types.app_block_builder_list.deserialize_aws_json_1_1(
                data["AppBlockBuilders"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
