"""Generated from Smithy shape ``com.amazonaws.glue#AutoDataQuality``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boolean_value
    import capo_glue.types.enclosed_in_string_property


class AutoDataQuality(TypedDict, closed=True):
    is_enabled: "capo_glue.types.boolean_value.BooleanValue"
    """<p>Specifies whether automatic data quality evaluation is enabled. When set to <code>true</code>, data quality checks are performed automatically.</p>"""
    evaluation_context: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The evaluation context for the automatic data quality checks. This defines the scope and parameters for the data quality evaluation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoDataQuality) -> dict:
    out: dict = {}
    out["IsEnabled"] = value.get("is_enabled", False)
    if "evaluation_context" in value:
        out["EvaluationContext"] = value["evaluation_context"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoDataQuality:
    out: AutoDataQuality = {}  # type: ignore[typeddict-item]
    if "IsEnabled" in data:
        out["is_enabled"] = data["IsEnabled"]
    else:
        out["is_enabled"] = False
    if "EvaluationContext" in data:
        out["evaluation_context"] = data["EvaluationContext"]
    return out
