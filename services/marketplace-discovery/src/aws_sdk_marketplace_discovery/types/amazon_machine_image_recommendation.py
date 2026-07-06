"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AmazonMachineImageRecommendation``."""

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError


class AmazonMachineImageRecommendation(TypedDict, closed=True):
    instance_type: "str"
    """<p>The recommended EC2 instance type for this AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonMachineImageRecommendation) -> dict:
    out: dict = {}
    out["instanceType"] = value["instance_type"]
    return out


def deserialize_json(data: dict) -> AmazonMachineImageRecommendation:
    out: AmazonMachineImageRecommendation = {}  # type: ignore[typeddict-item]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    else:
        raise DeserializationError(
            "AmazonMachineImageRecommendation.instance_type required"
        )
    return out
