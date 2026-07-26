"""Generated from Smithy shape ``com.amazonaws.clouddirectory#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.rule_parameter_map
    import capo_clouddirectory.types.rule_type


class Rule(TypedDict, closed=True):
    type: NotRequired["capo_clouddirectory.types.rule_type.RuleType"]
    """<p>The type of attribute validation rule.</p>"""
    parameters: NotRequired[
        "capo_clouddirectory.types.rule_parameter_map.RuleParameterMap"
    ]
    """<p>The minimum and maximum parameters that are associated with the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Rule) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_clouddirectory.types.rule_type

        out["Type"] = capo_clouddirectory.types.rule_type.serialize_json(value["type"])
    if "parameters" in value:
        import capo_clouddirectory.types.rule_parameter_map

        out["Parameters"] = capo_clouddirectory.types.rule_parameter_map.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_clouddirectory.types.rule_type

        out["type"] = capo_clouddirectory.types.rule_type.deserialize_json(data["Type"])
    if "Parameters" in data:
        import capo_clouddirectory.types.rule_parameter_map

        out["parameters"] = (
            capo_clouddirectory.types.rule_parameter_map.deserialize_json(
                data["Parameters"]
            )
        )
    return out
