"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateTargetDomainOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_securityagent.types.target_domain_id
    import aws_sdk_securityagent.types.target_domain_status
    import aws_sdk_securityagent.types.verification_details


class UpdateTargetDomainOutput(TypedDict):
    target_domain_id: "aws_sdk_securityagent.types.target_domain_id.TargetDomainId"
    """<p>The unique identifier of the target domain.</p>"""
    domain_name: "str"
    """<p>The domain name of the target domain.</p>"""
    verification_status: (
        "aws_sdk_securityagent.types.target_domain_status.TargetDomainStatus"
    )
    """<p>The current verification status of the target domain.</p>"""
    verification_status_reason: NotRequired["str"]
    """<p>The reason for the current target domain verification status.</p>"""
    verification_details: NotRequired[
        "aws_sdk_securityagent.types.verification_details.VerificationDetails"
    ]
    """<p>The updated verification details for the target domain.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the target domain was created, in UTC format.</p>"""
    verified_at: NotRequired["datetime.datetime"]
    """<p>The date and time the target domain was verified, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTargetDomainOutput) -> dict:
    out: dict = {}
    out["targetDomainId"] = value["target_domain_id"]
    out["domainName"] = value["domain_name"]
    import aws_sdk_securityagent.types.target_domain_status

    out["verificationStatus"] = (
        aws_sdk_securityagent.types.target_domain_status.serialize_json(
            value["verification_status"]
        )
    )
    if "verification_status_reason" in value:
        out["verificationStatusReason"] = value["verification_status_reason"]
    if "verification_details" in value:
        import aws_sdk_securityagent.types.verification_details

        out["verificationDetails"] = (
            aws_sdk_securityagent.types.verification_details.serialize_json(
                value["verification_details"]
            )
        )
    if "created_at" in value:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "verified_at" in value:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["verifiedAt"] = (
            aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
                value["verified_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTargetDomainOutput:
    out: UpdateTargetDomainOutput = {}  # type: ignore[typeddict-item]
    if "targetDomainId" in data:
        out["target_domain_id"] = data["targetDomainId"]
    else:
        raise DeserializationError("UpdateTargetDomainOutput.target_domain_id required")
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("UpdateTargetDomainOutput.domain_name required")
    if "verificationStatus" in data:
        import aws_sdk_securityagent.types.target_domain_status

        out["verification_status"] = (
            aws_sdk_securityagent.types.target_domain_status.deserialize_json(
                data["verificationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTargetDomainOutput.verification_status required"
        )
    if "verificationStatusReason" in data:
        out["verification_status_reason"] = data["verificationStatusReason"]
    if "verificationDetails" in data:
        import aws_sdk_securityagent.types.verification_details

        out["verification_details"] = (
            aws_sdk_securityagent.types.verification_details.deserialize_json(
                data["verificationDetails"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "verifiedAt" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["verified_at"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["verifiedAt"]
            )
        )
    return out
