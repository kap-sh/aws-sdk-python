"""Generated from Smithy shape ``com.amazonaws.securityhub#IntegerListConfigurationOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.integer_list


class IntegerListConfigurationOptions(TypedDict):
    default_value: NotRequired["aws_sdk_securityhub.types.integer_list.IntegerList"]
    """<p> The Security Hub CSPM default value for a control parameter that is a list of integers. </p>"""
    min: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The minimum valid value for a control parameter that is a list of integers. </p>"""
    max: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The maximum valid value for a control parameter that is a list of integers. </p>"""
    max_items: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The maximum number of list items that an interger list control parameter can accept. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerListConfigurationOptions) -> dict:
    out: dict = {}
    if "default_value" in value:
        import aws_sdk_securityhub.types.integer_list

        out["DefaultValue"] = aws_sdk_securityhub.types.integer_list.serialize_json(
            value["default_value"]
        )
    if "min" in value:
        out["Min"] = value["min"]
    if "max" in value:
        out["Max"] = value["max"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    return out


def deserialize_json(data: dict) -> IntegerListConfigurationOptions:
    out: IntegerListConfigurationOptions = {}  # type: ignore[typeddict-item]
    if "DefaultValue" in data:
        import aws_sdk_securityhub.types.integer_list

        out["default_value"] = aws_sdk_securityhub.types.integer_list.deserialize_json(
            data["DefaultValue"]
        )
    if "Min" in data:
        out["min"] = data["Min"]
    if "Max" in data:
        out["max"] = data["Max"]
    if "MaxItems" in data:
        out["max_items"] = data["MaxItems"]
    return out
