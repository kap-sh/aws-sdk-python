"""Generated from Smithy shape ``com.amazonaws.securityhub#EnumListConfigurationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.string_list


class EnumListConfigurationOptions(TypedDict, closed=True):
    default_value: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p> The Security Hub CSPM default value for a control parameter that is a list of enums. </p>"""
    max_items: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The maximum number of list items that an enum list control parameter can accept. </p>"""
    allowed_values: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p> The valid values for a control parameter that is a list of enums. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnumListConfigurationOptions) -> dict:
    out: dict = {}
    if "default_value" in value:
        import aws_sdk_securityhub.types.string_list

        out["DefaultValue"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["default_value"]
        )
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    if "allowed_values" in value:
        import aws_sdk_securityhub.types.string_list

        out["AllowedValues"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["allowed_values"]
        )
    return out


def deserialize_json(data: dict) -> EnumListConfigurationOptions:
    out: EnumListConfigurationOptions = {}  # type: ignore[typeddict-item]
    if "DefaultValue" in data:
        import aws_sdk_securityhub.types.string_list

        out["default_value"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["DefaultValue"]
        )
    if "MaxItems" in data:
        out["max_items"] = data["MaxItems"]
    if "AllowedValues" in data:
        import aws_sdk_securityhub.types.string_list

        out["allowed_values"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["AllowedValues"]
        )
    return out
