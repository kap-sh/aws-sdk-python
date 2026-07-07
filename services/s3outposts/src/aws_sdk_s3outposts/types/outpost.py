"""Generated from Smithy shape ``com.amazonaws.s3outposts#Outpost``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3outposts.types.aws_account_id
    import aws_sdk_s3outposts.types.capacity_in_bytes
    import aws_sdk_s3outposts.types.outpost_arn
    import aws_sdk_s3outposts.types.outpost_id
    import aws_sdk_s3outposts.types.s3_outpost_arn


class Outpost(TypedDict, closed=True):
    outpost_arn: NotRequired["aws_sdk_s3outposts.types.outpost_arn.OutpostArn"]
    """<p>Specifies the unique Amazon Resource Name (ARN) for the outpost.</p>"""
    s3_outpost_arn: NotRequired["aws_sdk_s3outposts.types.s3_outpost_arn.S3OutpostArn"]
    """<p>Specifies the unique S3 on Outposts ARN for use with Resource Access Manager (RAM).</p>"""
    outpost_id: NotRequired["aws_sdk_s3outposts.types.outpost_id.OutpostId"]
    """<p>Specifies the unique identifier for the outpost.</p>"""
    owner_id: NotRequired["aws_sdk_s3outposts.types.aws_account_id.AwsAccountId"]
    """<p>Returns the Amazon Web Services account ID of the outpost owner. Useful for comparing owned versus shared outposts.</p>"""
    capacity_in_bytes: "aws_sdk_s3outposts.types.capacity_in_bytes.CapacityInBytes"
    """<p>The Amazon S3 capacity of the outpost in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Outpost) -> dict:
    out: dict = {}
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
    if "s3_outpost_arn" in value:
        out["S3OutpostArn"] = value["s3_outpost_arn"]
    if "outpost_id" in value:
        out["OutpostId"] = value["outpost_id"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    out["CapacityInBytes"] = value.get("capacity_in_bytes", 0)
    return out


def deserialize_json(data: dict) -> Outpost:
    out: Outpost = {}  # type: ignore[typeddict-item]
    if "OutpostArn" in data:
        out["outpost_arn"] = data["OutpostArn"]
    if "S3OutpostArn" in data:
        out["s3_outpost_arn"] = data["S3OutpostArn"]
    if "OutpostId" in data:
        out["outpost_id"] = data["OutpostId"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "CapacityInBytes" in data:
        out["capacity_in_bytes"] = data["CapacityInBytes"]
    else:
        out["capacity_in_bytes"] = 0
    return out
