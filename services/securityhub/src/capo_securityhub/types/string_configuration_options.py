"""Generated from Smithy shape ``com.amazonaws.securityhub#StringConfigurationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class StringConfigurationOptions(TypedDict, closed=True):
    default_value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Security Hub CSPM default value for a control parameter that is a string. </p>"""
    re2_expression: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> An RE2 regular expression that Security Hub CSPM uses to validate a user-provided control parameter string. </p>"""
    expression_description: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The description of the RE2 regular expression. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringConfigurationOptions) -> dict:
    out: dict = {}
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "re2_expression" in value:
        out["Re2Expression"] = value["re2_expression"]
    if "expression_description" in value:
        out["ExpressionDescription"] = value["expression_description"]
    return out


def deserialize_json(data: dict) -> StringConfigurationOptions:
    out: StringConfigurationOptions = {}  # type: ignore[typeddict-item]
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    if "Re2Expression" in data:
        out["re2_expression"] = data["Re2Expression"]
    if "ExpressionDescription" in data:
        out["expression_description"] = data["ExpressionDescription"]
    return out
