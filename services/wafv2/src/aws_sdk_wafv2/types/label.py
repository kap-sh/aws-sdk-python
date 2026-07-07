"""Generated from Smithy shape ``com.amazonaws.wafv2#Label``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.label_name


class Label(TypedDict, closed=True):
    name: "aws_sdk_wafv2.types.label_name.LabelName"
    """<p>The label string. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Label) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Label:
    out: Label = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Label.name required")
    return out
