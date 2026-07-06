"""Generated from Smithy shape ``com.amazonaws.frauddetector#FilterCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.filter_string


class FilterCondition(TypedDict, closed=True):
    value: NotRequired["aws_sdk_frauddetector.types.filter_string.filterString"]
    """<p> A statement containing a resource property and a value to specify filter condition. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterCondition) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterCondition:
    out: FilterCondition = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    return out
