"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeImagesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.image_list
    import aws_sdk_appstream.types.string


class DescribeImagesResult(TypedDict):
    images: NotRequired["aws_sdk_appstream.types.image_list.ImageList"]
    """<p>Information about the images.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImagesResult) -> dict:
    out: dict = {}
    if "images" in value:
        import aws_sdk_appstream.types.image_list

        out["Images"] = aws_sdk_appstream.types.image_list.serialize_aws_json_1_1(
            value["images"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImagesResult:
    out: DescribeImagesResult = {}  # type: ignore[typeddict-item]
    if "Images" in data:
        import aws_sdk_appstream.types.image_list

        out["images"] = aws_sdk_appstream.types.image_list.deserialize_aws_json_1_1(
            data["Images"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
