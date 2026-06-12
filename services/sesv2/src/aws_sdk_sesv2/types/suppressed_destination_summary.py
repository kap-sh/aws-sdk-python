"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressedDestinationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_address
    import aws_sdk_sesv2.types.suppression_list_reason
    import aws_sdk_sesv2.types.timestamp


class SuppressedDestinationSummary(TypedDict):
    email_address: "aws_sdk_sesv2.types.email_address.EmailAddress"
    """<p>The email address that's on the suppression list for your account or for a specific tenant.</p>"""
    reason: "aws_sdk_sesv2.types.suppression_list_reason.SuppressionListReason"
    """<p>The reason that the address was added to the suppression list for your account or for a specific tenant.</p>"""
    last_update_time: "aws_sdk_sesv2.types.timestamp.Timestamp"
    """<p>The date and time when the suppressed destination was last updated, shown in Unix time format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressedDestinationSummary) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
    import aws_sdk_sesv2.types.suppression_list_reason

    out["Reason"] = aws_sdk_sesv2.types.suppression_list_reason.serialize_json(
        value["reason"]
    )
    import aws_sdk_sesv2.types.timestamp

    out["LastUpdateTime"] = aws_sdk_sesv2.types.timestamp.serialize_json(
        value["last_update_time"]
    )
    return out


def deserialize_json(data: dict) -> SuppressedDestinationSummary:
    out: SuppressedDestinationSummary = {}  # type: ignore[typeddict-item]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError(
            "SuppressedDestinationSummary.email_address required"
        )
    if "Reason" in data:
        import aws_sdk_sesv2.types.suppression_list_reason

        out["reason"] = aws_sdk_sesv2.types.suppression_list_reason.deserialize_json(
            data["Reason"]
        )
    else:
        raise DeserializationError("SuppressedDestinationSummary.reason required")
    if "LastUpdateTime" in data:
        import aws_sdk_sesv2.types.timestamp

        out["last_update_time"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["LastUpdateTime"]
        )
    else:
        raise DeserializationError(
            "SuppressedDestinationSummary.last_update_time required"
        )
    return out
