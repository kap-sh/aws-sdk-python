"""Generated from Smithy shape ``com.amazonaws.wafv2#LabelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.label_name


class LabelSummary(TypedDict, closed=True):
    name: NotRequired["aws_sdk_wafv2.types.label_name.LabelName"]
    """<p>An individual label specification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelSummary:
    out: LabelSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
