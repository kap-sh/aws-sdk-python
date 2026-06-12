"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeImageBuildersResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.image_builder_list
    import aws_sdk_appstream.types.string


class DescribeImageBuildersResult(TypedDict):
    image_builders: NotRequired[
        "aws_sdk_appstream.types.image_builder_list.ImageBuilderList"
    ]
    """<p>Information about the image builders.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageBuildersResult) -> dict:
    out: dict = {}
    if "image_builders" in value:
        import aws_sdk_appstream.types.image_builder_list

        out["ImageBuilders"] = (
            aws_sdk_appstream.types.image_builder_list.serialize_aws_json_1_1(
                value["image_builders"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageBuildersResult:
    out: DescribeImageBuildersResult = {}  # type: ignore[typeddict-item]
    if "ImageBuilders" in data:
        import aws_sdk_appstream.types.image_builder_list

        out["image_builders"] = (
            aws_sdk_appstream.types.image_builder_list.deserialize_aws_json_1_1(
                data["ImageBuilders"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
