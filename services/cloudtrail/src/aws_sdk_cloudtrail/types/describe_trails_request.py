"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DescribeTrailsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.boolean
    import aws_sdk_cloudtrail.types.trail_name_list


class DescribeTrailsRequest(TypedDict):
    trail_name_list: NotRequired[
        "aws_sdk_cloudtrail.types.trail_name_list.TrailNameList"
    ]
    """<p>Specifies a list of trail names, trail ARNs, or both, of the trails to describe. The format of a trail ARN is:</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p> <p>If an empty list is specified, information for the trail in the current Region is returned.</p> <ul> <li> <p>If an empty list is specified and <code>IncludeShadowTrails</code> is false, then information for all trails in the current Region is returned.</p> </li> <li> <p>If an empty list is specified and IncludeShadowTrails is null or true, then information for all trails in the current Region and any associated shadow trails in other Regions is returned.</p> </li> </ul> <note> <p>If one or more trail names are specified, information is returned only if the names match the names of trails belonging only to the current Region and current account. To return information about a trail in another Region, you must specify its trail ARN.</p> </note>"""
    include_shadow_trails: NotRequired["aws_sdk_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether to include shadow trails in the response. A shadow trail is the replication in a Region of a trail that was created in a different Region, or in the case of an organization trail, the replication of an organization trail in member accounts. If you do not include shadow trails, organization trails in a member account and Region replication trails will not be returned. The default is true.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrailsRequest) -> dict:
    out: dict = {}
    if "trail_name_list" in value:
        import aws_sdk_cloudtrail.types.trail_name_list

        out["trailNameList"] = (
            aws_sdk_cloudtrail.types.trail_name_list.serialize_aws_json_1_1(
                value["trail_name_list"]
            )
        )
    if "include_shadow_trails" in value:
        out["includeShadowTrails"] = value["include_shadow_trails"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrailsRequest:
    out: DescribeTrailsRequest = {}  # type: ignore[typeddict-item]
    if "trailNameList" in data:
        import aws_sdk_cloudtrail.types.trail_name_list

        out["trail_name_list"] = (
            aws_sdk_cloudtrail.types.trail_name_list.deserialize_aws_json_1_1(
                data["trailNameList"]
            )
        )
    if "includeShadowTrails" in data:
        out["include_shadow_trails"] = data["includeShadowTrails"]
    return out
