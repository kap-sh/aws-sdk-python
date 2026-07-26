"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.suppression_list_reasons
    import capo_sesv2.types.suppression_validation_attributes


class SuppressionAttributes(TypedDict, closed=True):
    suppressed_reasons: NotRequired[
        "capo_sesv2.types.suppression_list_reasons.SuppressionListReasons"
    ]
    """<p>A list that contains the reasons that email addresses will be automatically added to the suppression list for your account. This list can contain any or all of the following:</p> <ul> <li> <p> <code>COMPLAINT</code> – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a complaint.</p> </li> <li> <p> <code>BOUNCE</code> – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a hard bounce.</p> </li> </ul>"""
    validation_attributes: NotRequired[
        "capo_sesv2.types.suppression_validation_attributes.SuppressionValidationAttributes"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionAttributes) -> dict:
    out: dict = {}
    if "suppressed_reasons" in value:
        import capo_sesv2.types.suppression_list_reasons

        out["SuppressedReasons"] = (
            capo_sesv2.types.suppression_list_reasons.serialize_json(
                value["suppressed_reasons"]
            )
        )
    if "validation_attributes" in value:
        import capo_sesv2.types.suppression_validation_attributes

        out["ValidationAttributes"] = (
            capo_sesv2.types.suppression_validation_attributes.serialize_json(
                value["validation_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> SuppressionAttributes:
    out: SuppressionAttributes = {}  # type: ignore[typeddict-item]
    if "SuppressedReasons" in data:
        import capo_sesv2.types.suppression_list_reasons

        out["suppressed_reasons"] = (
            capo_sesv2.types.suppression_list_reasons.deserialize_json(
                data["SuppressedReasons"]
            )
        )
    if "ValidationAttributes" in data:
        import capo_sesv2.types.suppression_validation_attributes

        out["validation_attributes"] = (
            capo_sesv2.types.suppression_validation_attributes.deserialize_json(
                data["ValidationAttributes"]
            )
        )
    return out
