"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#MixedInstanceConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class MixedInstanceConfiguration(TypedDict, closed=True):
    type: NotRequired["str"]
    """<p>The instance type of the configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MixedInstanceConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MixedInstanceConfiguration:
    out: MixedInstanceConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    return out
