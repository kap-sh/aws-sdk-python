"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionValidationOptions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.suppression_condition_threshold


class SuppressionValidationOptions(TypedDict):
    condition_threshold: "aws_sdk_sesv2.types.suppression_condition_threshold.SuppressionConditionThreshold"
    """<p>Specifies the condition threshold settings for suppression validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionValidationOptions) -> dict:
    out: dict = {}
    import aws_sdk_sesv2.types.suppression_condition_threshold

    out["ConditionThreshold"] = (
        aws_sdk_sesv2.types.suppression_condition_threshold.serialize_json(
            value["condition_threshold"]
        )
    )
    return out


def deserialize_json(data: dict) -> SuppressionValidationOptions:
    out: SuppressionValidationOptions = {}  # type: ignore[typeddict-item]
    if "ConditionThreshold" in data:
        import aws_sdk_sesv2.types.suppression_condition_threshold

        out["condition_threshold"] = (
            aws_sdk_sesv2.types.suppression_condition_threshold.deserialize_json(
                data["ConditionThreshold"]
            )
        )
    else:
        raise DeserializationError(
            "SuppressionValidationOptions.condition_threshold required"
        )
    return out
