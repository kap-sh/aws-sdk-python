"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeImagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.arn_list
    import aws_sdk_appstream.types.describe_images_max_results
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.string_list
    import aws_sdk_appstream.types.visibility_type


class DescribeImagesRequest(TypedDict, closed=True):
    names: NotRequired["aws_sdk_appstream.types.string_list.StringList"]
    """<p>The names of the public or private images to describe.</p>"""
    arns: NotRequired["aws_sdk_appstream.types.arn_list.ArnList"]
    """<p>The ARNs of the public, private, and shared images to describe.</p>"""
    type: NotRequired["aws_sdk_appstream.types.visibility_type.VisibilityType"]
    """<p>The type of image (public, private, or shared) to describe. </p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""
    max_results: NotRequired[
        "aws_sdk_appstream.types.describe_images_max_results.DescribeImagesMaxResults"
    ]
    """<p>The maximum size of each page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImagesRequest) -> dict:
    out: dict = {}
    if "names" in value:
        import aws_sdk_appstream.types.string_list

        out["Names"] = aws_sdk_appstream.types.string_list.serialize_aws_json_1_1(
            value["names"]
        )
    if "arns" in value:
        import aws_sdk_appstream.types.arn_list

        out["Arns"] = aws_sdk_appstream.types.arn_list.serialize_aws_json_1_1(
            value["arns"]
        )
    if "type" in value:
        import aws_sdk_appstream.types.visibility_type

        out["Type"] = aws_sdk_appstream.types.visibility_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImagesRequest:
    out: DescribeImagesRequest = {}  # type: ignore[typeddict-item]
    if "Names" in data:
        import aws_sdk_appstream.types.string_list

        out["names"] = aws_sdk_appstream.types.string_list.deserialize_aws_json_1_1(
            data["Names"]
        )
    if "Arns" in data:
        import aws_sdk_appstream.types.arn_list

        out["arns"] = aws_sdk_appstream.types.arn_list.deserialize_aws_json_1_1(
            data["Arns"]
        )
    if "Type" in data:
        import aws_sdk_appstream.types.visibility_type

        out["type"] = aws_sdk_appstream.types.visibility_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
