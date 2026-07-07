"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionValidationAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.suppression_condition_threshold


class SuppressionValidationAttributes(TypedDict, closed=True):
    condition_threshold: "aws_sdk_sesv2.types.suppression_condition_threshold.SuppressionConditionThreshold"
    """<p>Specifies the condition threshold settings for account-level suppression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionValidationAttributes) -> dict:
    out: dict = {}
    import aws_sdk_sesv2.types.suppression_condition_threshold

    out["ConditionThreshold"] = (
        aws_sdk_sesv2.types.suppression_condition_threshold.serialize_json(
            value["condition_threshold"]
        )
    )
    return out


def deserialize_json(data: dict) -> SuppressionValidationAttributes:
    out: SuppressionValidationAttributes = {}  # type: ignore[typeddict-item]
    if "ConditionThreshold" in data:
        import aws_sdk_sesv2.types.suppression_condition_threshold

        out["condition_threshold"] = (
            aws_sdk_sesv2.types.suppression_condition_threshold.deserialize_json(
                data["ConditionThreshold"]
            )
        )
    else:
        raise DeserializationError(
            "SuppressionValidationAttributes.condition_threshold required"
        )
    return out
