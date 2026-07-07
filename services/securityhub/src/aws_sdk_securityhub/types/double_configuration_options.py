"""Generated from Smithy shape ``com.amazonaws.securityhub#DoubleConfigurationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.double


class DoubleConfigurationOptions(TypedDict, closed=True):
    default_value: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p> The Security Hub CSPM default value for a control parameter that is a double. </p>"""
    min: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p> The minimum valid value for a control parameter that is a double. </p>"""
    max: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p> The maximum valid value for a control parameter that is a double. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DoubleConfigurationOptions) -> dict:
    out: dict = {}
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "min" in value:
        out["Min"] = value["min"]
    if "max" in value:
        out["Max"] = value["max"]
    return out


def deserialize_json(data: dict) -> DoubleConfigurationOptions:
    out: DoubleConfigurationOptions = {}  # type: ignore[typeddict-item]
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    if "Min" in data:
        out["min"] = data["Min"]
    if "Max" in data:
        out["max"] = data["Max"]
    return out
