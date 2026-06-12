"""Generated from Smithy shape ``com.amazonaws.securityhub#IntegerConfigurationOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer


class IntegerConfigurationOptions(TypedDict):
    default_value: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The Security Hub CSPM default value for a control parameter that is an integer. </p>"""
    min: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The minimum valid value for a control parameter that is an integer. </p>"""
    max: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The maximum valid value for a control parameter that is an integer. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerConfigurationOptions) -> dict:
    out: dict = {}
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "min" in value:
        out["Min"] = value["min"]
    if "max" in value:
        out["Max"] = value["max"]
    return out


def deserialize_json(data: dict) -> IntegerConfigurationOptions:
    out: IntegerConfigurationOptions = {}  # type: ignore[typeddict-item]
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    if "Min" in data:
        out["min"] = data["Min"]
    if "Max" in data:
        out["max"] = data["Max"]
    return out
