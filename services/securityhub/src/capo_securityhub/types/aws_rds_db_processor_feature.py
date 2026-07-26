"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbProcessorFeature``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsRdsDbProcessorFeature(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the processor feature. Valid values are <code>coreCount</code> or <code>threadsPerCore</code>.</p>"""
    value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value of the processor feature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbProcessorFeature) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbProcessorFeature:
    out: AwsRdsDbProcessorFeature = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
