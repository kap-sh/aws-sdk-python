"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#MpaStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.mpa_session_arn
    import aws_sdk_payment_cryptography.types.mpa_status_message
    import aws_sdk_payment_cryptography.types.session_status
    import aws_sdk_payment_cryptography.types.timestamp


class MpaStatus(TypedDict):
    mpa_session_arn: "aws_sdk_payment_cryptography.types.mpa_session_arn.MpaSessionArn"
    """<p>The ARN of the MPA session.</p>"""
    status: "aws_sdk_payment_cryptography.types.session_status.SessionStatus"
    """<p>The current status of the MPA session.</p>"""
    initiation_date: "aws_sdk_payment_cryptography.types.timestamp.Timestamp"
    """<p>The date and time when the MPA session was initiated.</p>"""
    status_message: NotRequired[
        "aws_sdk_payment_cryptography.types.mpa_status_message.MpaStatusMessage"
    ]
    """<p>The message providing additional information about the MPA session status.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MpaStatus) -> dict:
    out: dict = {}
    out["MpaSessionArn"] = value["mpa_session_arn"]
    out["Status"] = value["status"]
    import aws_sdk_payment_cryptography.types.timestamp

    out["InitiationDate"] = (
        aws_sdk_payment_cryptography.types.timestamp.serialize_aws_json_1_0(
            value["initiation_date"]
        )
    )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MpaStatus:
    out: MpaStatus = {}  # type: ignore[typeddict-item]
    if "MpaSessionArn" in data:
        out["mpa_session_arn"] = data["MpaSessionArn"]
    else:
        raise DeserializationError("MpaStatus.mpa_session_arn required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("MpaStatus.status required")
    if "InitiationDate" in data:
        import aws_sdk_payment_cryptography.types.timestamp

        out["initiation_date"] = (
            aws_sdk_payment_cryptography.types.timestamp.deserialize_aws_json_1_0(
                data["InitiationDate"]
            )
        )
    else:
        raise DeserializationError("MpaStatus.initiation_date required")
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
