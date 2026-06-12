"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#StartVerificationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.date_time
    import aws_sdk_partnercentral_account.types.verification_response_details
    import aws_sdk_partnercentral_account.types.verification_status
    import aws_sdk_partnercentral_account.types.verification_status_reason
    import aws_sdk_partnercentral_account.types.verification_type


class StartVerificationResponse(TypedDict):
    verification_type: (
        "aws_sdk_partnercentral_account.types.verification_type.VerificationType"
    )
    """<p>The type of verification that was started based on the provided verification details.</p>"""
    verification_status: (
        "aws_sdk_partnercentral_account.types.verification_status.VerificationStatus"
    )
    """<p>The initial status of the verification process after it has been started. Typically this will be pending or in-progress.</p>"""
    verification_status_reason: NotRequired[
        "aws_sdk_partnercentral_account.types.verification_status_reason.VerificationStatusReason"
    ]
    """<p>Additional information about the initial verification status, including any immediate feedback about the submitted verification details.</p>"""
    verification_response_details: "aws_sdk_partnercentral_account.types.verification_response_details.VerificationResponseDetails"
    """<p>Initial response details specific to the type of verification started, which may include next steps or additional requirements.</p>"""
    started_at: "aws_sdk_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the verification process was successfully initiated.</p>"""
    completed_at: NotRequired["aws_sdk_partnercentral_account.types.date_time.DateTime"]
    """<p>The timestamp when the verification process was completed. This field is typically null for newly started verifications unless they complete immediately.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartVerificationResponse) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_account.types.verification_type

    out["VerificationType"] = (
        aws_sdk_partnercentral_account.types.verification_type.serialize_aws_json_1_0(
            value["verification_type"]
        )
    )
    import aws_sdk_partnercentral_account.types.verification_status

    out["VerificationStatus"] = (
        aws_sdk_partnercentral_account.types.verification_status.serialize_aws_json_1_0(
            value["verification_status"]
        )
    )
    if "verification_status_reason" in value:
        out["VerificationStatusReason"] = value["verification_status_reason"]
    import aws_sdk_partnercentral_account.types.verification_response_details

    out["VerificationResponseDetails"] = (
        aws_sdk_partnercentral_account.types.verification_response_details.serialize_aws_json_1_0(
            value["verification_response_details"]
        )
    )
    import aws_sdk_partnercentral_account.types.date_time

    out["StartedAt"] = (
        aws_sdk_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["started_at"]
        )
    )
    if "completed_at" in value:
        import aws_sdk_partnercentral_account.types.date_time

        out["CompletedAt"] = (
            aws_sdk_partnercentral_account.types.date_time.serialize_aws_json_1_0(
                value["completed_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartVerificationResponse:
    out: StartVerificationResponse = {}  # type: ignore[typeddict-item]
    if "VerificationType" in data:
        import aws_sdk_partnercentral_account.types.verification_type

        out["verification_type"] = (
            aws_sdk_partnercentral_account.types.verification_type.deserialize_aws_json_1_0(
                data["VerificationType"]
            )
        )
    else:
        raise DeserializationError(
            "StartVerificationResponse.verification_type required"
        )
    if "VerificationStatus" in data:
        import aws_sdk_partnercentral_account.types.verification_status

        out["verification_status"] = (
            aws_sdk_partnercentral_account.types.verification_status.deserialize_aws_json_1_0(
                data["VerificationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "StartVerificationResponse.verification_status required"
        )
    if "VerificationStatusReason" in data:
        out["verification_status_reason"] = data["VerificationStatusReason"]
    if "VerificationResponseDetails" in data:
        import aws_sdk_partnercentral_account.types.verification_response_details

        out["verification_response_details"] = (
            aws_sdk_partnercentral_account.types.verification_response_details.deserialize_aws_json_1_0(
                data["VerificationResponseDetails"]
            )
        )
    else:
        raise DeserializationError(
            "StartVerificationResponse.verification_response_details required"
        )
    if "StartedAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["started_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["StartedAt"]
            )
        )
    else:
        raise DeserializationError("StartVerificationResponse.started_at required")
    if "CompletedAt" in data:
        import aws_sdk_partnercentral_account.types.date_time

        out["completed_at"] = (
            aws_sdk_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CompletedAt"]
            )
        )
    return out
