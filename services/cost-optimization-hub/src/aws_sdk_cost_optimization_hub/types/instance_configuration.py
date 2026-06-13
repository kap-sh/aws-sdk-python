"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#InstanceConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class InstanceConfiguration(TypedDict):
    type: NotRequired["str"]
    """<p>The instance type of the configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceConfiguration:
    out: InstanceConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    return out
