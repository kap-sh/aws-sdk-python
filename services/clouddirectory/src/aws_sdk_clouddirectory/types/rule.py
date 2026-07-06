"""Generated from Smithy shape ``com.amazonaws.clouddirectory#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.rule_parameter_map
    import aws_sdk_clouddirectory.types.rule_type


class Rule(TypedDict, closed=True):
    type: NotRequired["aws_sdk_clouddirectory.types.rule_type.RuleType"]
    """<p>The type of attribute validation rule.</p>"""
    parameters: NotRequired[
        "aws_sdk_clouddirectory.types.rule_parameter_map.RuleParameterMap"
    ]
    """<p>The minimum and maximum parameters that are associated with the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Rule) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_clouddirectory.types.rule_type

        out["Type"] = aws_sdk_clouddirectory.types.rule_type.serialize_json(
            value["type"]
        )
    if "parameters" in value:
        import aws_sdk_clouddirectory.types.rule_parameter_map

        out["Parameters"] = (
            aws_sdk_clouddirectory.types.rule_parameter_map.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_clouddirectory.types.rule_type

        out["type"] = aws_sdk_clouddirectory.types.rule_type.deserialize_json(
            data["Type"]
        )
    if "Parameters" in data:
        import aws_sdk_clouddirectory.types.rule_parameter_map

        out["parameters"] = (
            aws_sdk_clouddirectory.types.rule_parameter_map.deserialize_json(
                data["Parameters"]
            )
        )
    return out
