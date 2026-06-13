"""Generated from Smithy shape ``com.amazonaws.drs#SourceCloudProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.account_id
    import aws_sdk_drs.types.aws_availability_zone
    import aws_sdk_drs.types.aws_region
    import aws_sdk_drs.types.outpost_arn


class SourceCloudProperties(TypedDict):
    origin_account_id: NotRequired["aws_sdk_drs.types.account_id.AccountID"]
    """<p>AWS Account ID for an EC2-originated Source Server.</p>"""
    origin_region: NotRequired["aws_sdk_drs.types.aws_region.AwsRegion"]
    """<p>AWS Region for an EC2-originated Source Server.</p>"""
    origin_availability_zone: NotRequired[
        "aws_sdk_drs.types.aws_availability_zone.AwsAvailabilityZone"
    ]
    """<p>AWS Availability Zone for an EC2-originated Source Server.</p>"""
    source_outpost_arn: NotRequired["aws_sdk_drs.types.outpost_arn.OutpostARN"]
    """<p>The ARN of the source Outpost</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceCloudProperties) -> dict:
    out: dict = {}
    if "origin_account_id" in value:
        out["originAccountID"] = value["origin_account_id"]
    if "origin_region" in value:
        out["originRegion"] = value["origin_region"]
    if "origin_availability_zone" in value:
        out["originAvailabilityZone"] = value["origin_availability_zone"]
    if "source_outpost_arn" in value:
        out["sourceOutpostArn"] = value["source_outpost_arn"]
    return out


def deserialize_json(data: dict) -> SourceCloudProperties:
    out: SourceCloudProperties = {}  # type: ignore[typeddict-item]
    if "originAccountID" in data:
        out["origin_account_id"] = data["originAccountID"]
    if "originRegion" in data:
        out["origin_region"] = data["originRegion"]
    if "originAvailabilityZone" in data:
        out["origin_availability_zone"] = data["originAvailabilityZone"]
    if "sourceOutpostArn" in data:
        out["source_outpost_arn"] = data["sourceOutpostArn"]
    return out
