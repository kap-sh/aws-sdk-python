"""Generated from Smithy shape ``com.amazonaws.securityhub#StringListConfigurationOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class StringListConfigurationOptions(TypedDict):
    default_value: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p> The Security Hub CSPM default value for a control parameter that is a list of strings. </p>"""
    re2_expression: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> An RE2 regular expression that Security Hub CSPM uses to validate a user-provided list of strings for a control parameter. </p>"""
    max_items: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The maximum number of list items that a string list control parameter can accept. </p>"""
    expression_description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The description of the RE2 regular expression. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringListConfigurationOptions) -> dict:
    out: dict = {}
    if "default_value" in value:
        import aws_sdk_securityhub.types.string_list

        out["DefaultValue"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["default_value"]
        )
    if "re2_expression" in value:
        out["Re2Expression"] = value["re2_expression"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    if "expression_description" in value:
        out["ExpressionDescription"] = value["expression_description"]
    return out


def deserialize_json(data: dict) -> StringListConfigurationOptions:
    out: StringListConfigurationOptions = {}  # type: ignore[typeddict-item]
    if "DefaultValue" in data:
        import aws_sdk_securityhub.types.string_list

        out["default_value"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["DefaultValue"]
        )
    if "Re2Expression" in data:
        out["re2_expression"] = data["Re2Expression"]
    if "MaxItems" in data:
        out["max_items"] = data["MaxItems"]
    if "ExpressionDescription" in data:
        out["expression_description"] = data["ExpressionDescription"]
    return out
