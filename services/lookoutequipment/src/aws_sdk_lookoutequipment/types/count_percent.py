"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CountPercent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.float
    import aws_sdk_lookoutequipment.types.integer


class CountPercent(TypedDict, closed=True):
    count: "aws_sdk_lookoutequipment.types.integer.Integer"
    """<p> Indicates the count of occurences of the given statistic. </p>"""
    percentage: "aws_sdk_lookoutequipment.types.float.Float"
    """<p> Indicates the percentage of occurances of the given statistic. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CountPercent) -> dict:
    out: dict = {}
    out["Count"] = value["count"]
    out["Percentage"] = value.get("percentage", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> CountPercent:
    out: CountPercent = {}  # type: ignore[typeddict-item]
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        raise DeserializationError("CountPercent.count required")
    if "Percentage" in data:
        out["percentage"] = data["Percentage"]
    else:
        out["percentage"] = 0
    return out
