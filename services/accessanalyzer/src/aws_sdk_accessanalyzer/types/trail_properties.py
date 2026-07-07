"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#TrailProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.cloud_trail_arn
    import aws_sdk_accessanalyzer.types.region_list


class TrailProperties(TypedDict, closed=True):
    cloud_trail_arn: "aws_sdk_accessanalyzer.types.cloud_trail_arn.CloudTrailArn"
    """<p>Specifies the ARN of the trail. The format of a trail ARN is <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code>.</p>"""
    regions: NotRequired["aws_sdk_accessanalyzer.types.region_list.RegionList"]
    """<p>A list of regions to get CloudTrail data from and analyze to generate a policy.</p>"""
    all_regions: NotRequired["bool"]
    """<p>Possible values are <code>true</code> or <code>false</code>. If set to <code>true</code>, IAM Access Analyzer retrieves CloudTrail data from all regions to analyze and generate a policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrailProperties) -> dict:
    out: dict = {}
    out["cloudTrailArn"] = value["cloud_trail_arn"]
    if "regions" in value:
        import aws_sdk_accessanalyzer.types.region_list

        out["regions"] = aws_sdk_accessanalyzer.types.region_list.serialize_json(
            value["regions"]
        )
    if "all_regions" in value:
        out["allRegions"] = value["all_regions"]
    return out


def deserialize_json(data: dict) -> TrailProperties:
    out: TrailProperties = {}  # type: ignore[typeddict-item]
    if "cloudTrailArn" in data:
        out["cloud_trail_arn"] = data["cloudTrailArn"]
    else:
        raise DeserializationError("TrailProperties.cloud_trail_arn required")
    if "regions" in data:
        import aws_sdk_accessanalyzer.types.region_list

        out["regions"] = aws_sdk_accessanalyzer.types.region_list.deserialize_json(
            data["regions"]
        )
    if "allRegions" in data:
        out["all_regions"] = data["allRegions"]
    return out
