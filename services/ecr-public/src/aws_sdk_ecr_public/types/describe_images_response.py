"""Generated from Smithy shape ``com.amazonaws.ecrpublic#DescribeImagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.image_detail_list
    import aws_sdk_ecr_public.types.next_token


class DescribeImagesResponse(TypedDict, closed=True):
    image_details: NotRequired[
        "aws_sdk_ecr_public.types.image_detail_list.ImageDetailList"
    ]
    """<p>A list of <a>ImageDetail</a> objects that contain data about the image.</p>"""
    next_token: NotRequired["aws_sdk_ecr_public.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeImages</code> request. When the results of a <code>DescribeImages</code> request exceed <code>maxResults</code>, you can use this value to retrieve the next page of results. If there are no more results to return, this value is <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImagesResponse) -> dict:
    out: dict = {}
    if "image_details" in value:
        import aws_sdk_ecr_public.types.image_detail_list

        out["imageDetails"] = (
            aws_sdk_ecr_public.types.image_detail_list.serialize_aws_json_1_1(
                value["image_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImagesResponse:
    out: DescribeImagesResponse = {}  # type: ignore[typeddict-item]
    if "imageDetails" in data:
        import aws_sdk_ecr_public.types.image_detail_list

        out["image_details"] = (
            aws_sdk_ecr_public.types.image_detail_list.deserialize_aws_json_1_1(
                data["imageDetails"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
