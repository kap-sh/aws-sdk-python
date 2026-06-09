"""Generated from Smithy shape ``com.amazonaws.kms#MultiRegionKey``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.arn_type
    import aws_sdk_kms.types.region_type


class MultiRegionKey(TypedDict):
    arn: NotRequired["aws_sdk_kms.types.arn_type.ArnType"]
    """<p>Displays the key ARN of a primary or replica key of a multi-Region key.</p>"""
    region: NotRequired["aws_sdk_kms.types.region_type.RegionType"]
    """<p>Displays the Amazon Web Services Region of a primary or replica key in a multi-Region key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MultiRegionKey) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MultiRegionKey:
    out: MultiRegionKey = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Region" in data:
        out["region"] = data["Region"]
    return out
