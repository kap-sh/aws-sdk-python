"""Generated from Smithy shape ``com.amazonaws.kms#MultiRegionKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.arn_type
    import capo_kms.types.region_type


class MultiRegionKey(TypedDict, closed=True):
    arn: NotRequired["capo_kms.types.arn_type.ArnType"]
    """<p>Displays the key ARN of a primary or replica key of a multi-Region key.</p>"""
    region: NotRequired["capo_kms.types.region_type.RegionType"]
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
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    return out
