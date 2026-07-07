"""Generated from Smithy shape ``com.amazonaws.securityhub#BooleanConfigurationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean


class BooleanConfigurationOptions(TypedDict, closed=True):
    default_value: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> The Security Hub CSPM default value for a boolean parameter. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BooleanConfigurationOptions) -> dict:
    out: dict = {}
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> BooleanConfigurationOptions:
    out: BooleanConfigurationOptions = {}  # type: ignore[typeddict-item]
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    return out
