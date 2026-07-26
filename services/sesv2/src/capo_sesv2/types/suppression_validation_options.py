"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionValidationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.suppression_condition_threshold


class SuppressionValidationOptions(TypedDict, closed=True):
    condition_threshold: (
        "capo_sesv2.types.suppression_condition_threshold.SuppressionConditionThreshold"
    )
    """<p>Specifies the condition threshold settings for suppression validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionValidationOptions) -> dict:
    out: dict = {}
    import capo_sesv2.types.suppression_condition_threshold

    out["ConditionThreshold"] = (
        capo_sesv2.types.suppression_condition_threshold.serialize_json(
            value["condition_threshold"]
        )
    )
    return out


def deserialize_json(data: dict) -> SuppressionValidationOptions:
    out: SuppressionValidationOptions = {}  # type: ignore[typeddict-item]
    if "ConditionThreshold" in data:
        import capo_sesv2.types.suppression_condition_threshold

        out["condition_threshold"] = (
            capo_sesv2.types.suppression_condition_threshold.deserialize_json(
                data["ConditionThreshold"]
            )
        )
    else:
        raise DeserializationError(
            "SuppressionValidationOptions.condition_threshold required"
        )
    return out
