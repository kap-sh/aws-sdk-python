"""Generated from Smithy shape ``com.amazonaws.shield#SummarizedCounter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_shield.types.double
    import aws_sdk_shield.types.integer
    import aws_sdk_shield.types.string


class SummarizedCounter(TypedDict):
    name: NotRequired["aws_sdk_shield.types.string.String"]
    """<p>The counter name.</p>"""
    max: "aws_sdk_shield.types.double.Double"
    """<p>The maximum value of the counter for a specified time period.</p>"""
    average: "aws_sdk_shield.types.double.Double"
    """<p>The average value of the counter for a specified time period.</p>"""
    sum: "aws_sdk_shield.types.double.Double"
    """<p>The total of counter values for a specified time period.</p>"""
    n: "aws_sdk_shield.types.integer.Integer"
    """<p>The number of counters for a specified time period.</p>"""
    unit: NotRequired["aws_sdk_shield.types.string.String"]
    """<p>The unit of the counters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SummarizedCounter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    out["Max"] = value.get("max", 0)
    out["Average"] = value.get("average", 0)
    out["Sum"] = value.get("sum", 0)
    out["N"] = value.get("n", 0)
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SummarizedCounter:
    out: SummarizedCounter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Max" in data:
        out["max"] = data["Max"]
    else:
        out["max"] = 0
    if "Average" in data:
        out["average"] = data["Average"]
    else:
        out["average"] = 0
    if "Sum" in data:
        out["sum"] = data["Sum"]
    else:
        out["sum"] = 0
    if "N" in data:
        out["n"] = data["N"]
    else:
        out["n"] = 0
    if "Unit" in data:
        out["unit"] = data["Unit"]
    return out
