"""Generated from Smithy shape ``com.amazonaws.sesv2#PutAccountSuppressionAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.suppression_list_reasons
    import aws_sdk_sesv2.types.suppression_validation_attributes


class PutAccountSuppressionAttributesRequest(TypedDict):
    suppressed_reasons: NotRequired[
        "aws_sdk_sesv2.types.suppression_list_reasons.SuppressionListReasons"
    ]
    """<p>A list that contains the reasons that email addresses will be automatically added to the suppression list for your account. This list can contain any or all of the following:</p> <ul> <li> <p> <code>COMPLAINT</code> – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a complaint.</p> </li> <li> <p> <code>BOUNCE</code> – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a hard bounce.</p> </li> </ul>"""
    validation_attributes: NotRequired[
        "aws_sdk_sesv2.types.suppression_validation_attributes.SuppressionValidationAttributes"
    ]
    """<p>An object that contains additional suppression attributes for your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountSuppressionAttributesRequest) -> dict:
    out: dict = {}
    if "suppressed_reasons" in value:
        import aws_sdk_sesv2.types.suppression_list_reasons

        out["SuppressedReasons"] = (
            aws_sdk_sesv2.types.suppression_list_reasons.serialize_json(
                value["suppressed_reasons"]
            )
        )
    if "validation_attributes" in value:
        import aws_sdk_sesv2.types.suppression_validation_attributes

        out["ValidationAttributes"] = (
            aws_sdk_sesv2.types.suppression_validation_attributes.serialize_json(
                value["validation_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutAccountSuppressionAttributesRequest:
    out: PutAccountSuppressionAttributesRequest = {}  # type: ignore[typeddict-item]
    if "SuppressedReasons" in data:
        import aws_sdk_sesv2.types.suppression_list_reasons

        out["suppressed_reasons"] = (
            aws_sdk_sesv2.types.suppression_list_reasons.deserialize_json(
                data["SuppressedReasons"]
            )
        )
    if "ValidationAttributes" in data:
        import aws_sdk_sesv2.types.suppression_validation_attributes

        out["validation_attributes"] = (
            aws_sdk_sesv2.types.suppression_validation_attributes.deserialize_json(
                data["ValidationAttributes"]
            )
        )
    return out
