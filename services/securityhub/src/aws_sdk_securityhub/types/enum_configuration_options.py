"""Generated from Smithy shape ``com.amazonaws.securityhub#EnumConfigurationOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class EnumConfigurationOptions(TypedDict):
    default_value: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Security Hub CSPM default value for a control parameter that is an enum. </p>"""
    allowed_values: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p> The valid values for a control parameter that is an enum. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnumConfigurationOptions) -> dict:
    out: dict = {}
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "allowed_values" in value:
        import aws_sdk_securityhub.types.string_list

        out["AllowedValues"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["allowed_values"]
        )
    return out


def deserialize_json(data: dict) -> EnumConfigurationOptions:
    out: EnumConfigurationOptions = {}  # type: ignore[typeddict-item]
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    if "AllowedValues" in data:
        import aws_sdk_securityhub.types.string_list

        out["allowed_values"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["AllowedValues"]
        )
    return out
