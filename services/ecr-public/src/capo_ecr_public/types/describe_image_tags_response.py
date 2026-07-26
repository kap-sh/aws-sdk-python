"""Generated from Smithy shape ``com.amazonaws.ecrpublic#DescribeImageTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.image_tag_detail_list
    import capo_ecr_public.types.next_token


class DescribeImageTagsResponse(TypedDict, closed=True):
    image_tag_details: NotRequired[
        "capo_ecr_public.types.image_tag_detail_list.ImageTagDetailList"
    ]
    """<p>The image tag details for the images in the requested repository.</p>"""
    next_token: NotRequired["capo_ecr_public.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeImageTags</code> request. When the results of a <code>DescribeImageTags</code> request exceed <code>maxResults</code>, you can use this value to retrieve the next page of results. If there are no more results to return, this value is <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageTagsResponse) -> dict:
    out: dict = {}
    if "image_tag_details" in value:
        import capo_ecr_public.types.image_tag_detail_list

        out["imageTagDetails"] = (
            capo_ecr_public.types.image_tag_detail_list.serialize_aws_json_1_1(
                value["image_tag_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageTagsResponse:
    out: DescribeImageTagsResponse = {}  # type: ignore[typeddict-item]
    if "imageTagDetails" in data:
        import capo_ecr_public.types.image_tag_detail_list

        out["image_tag_details"] = (
            capo_ecr_public.types.image_tag_detail_list.deserialize_aws_json_1_1(
                data["imageTagDetails"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
