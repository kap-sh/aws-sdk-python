"""Generated from Smithy shape ``com.amazonaws.connect#Distribution``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.aws_region
    import aws_sdk_connect.types.percentage


class Distribution(TypedDict):
    region: "aws_sdk_connect.types.aws_region.AwsRegion"
    """<p>The Amazon Web Services Region where the traffic is distributed.</p>"""
    percentage: "aws_sdk_connect.types.percentage.Percentage"
    """<p>The percentage of the traffic that is distributed, in increments of 10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Distribution) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    out["Percentage"] = value.get("percentage", 0)
    return out


def deserialize_json(data: dict) -> Distribution:
    out: Distribution = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("Distribution.region required")
    if "Percentage" in data:
        out["percentage"] = data["Percentage"]
    else:
        out["percentage"] = 0
    return out
