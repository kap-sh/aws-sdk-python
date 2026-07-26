"""Generated from Smithy shape ``com.amazonaws.securityagent#VerifyTargetDomainOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.target_domain_id
    import capo_securityagent.types.target_domain_status


class VerifyTargetDomainOutput(TypedDict, closed=True):
    target_domain_id: NotRequired[
        "capo_securityagent.types.target_domain_id.TargetDomainId"
    ]
    """<p>The unique identifier of the target domain.</p>"""
    domain_name: NotRequired["str"]
    """<p>The domain name of the target domain.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the target domain was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the target domain was last updated, in UTC format.</p>"""
    verified_at: NotRequired["datetime.datetime"]
    """<p>The date and time the target domain was verified, in UTC format.</p>"""
    status: NotRequired[
        "capo_securityagent.types.target_domain_status.TargetDomainStatus"
    ]
    """<p>The verification status of the target domain.</p>"""
    verification_status_reason: NotRequired["str"]
    """<p>The reason for the current target domain verification status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyTargetDomainOutput) -> dict:
    out: dict = {}
    if "target_domain_id" in value:
        out["targetDomainId"] = value["target_domain_id"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "created_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["createdAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["updatedAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "verified_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["verifiedAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["verified_at"]
        )
    if "status" in value:
        import capo_securityagent.types.target_domain_status

        out["status"] = capo_securityagent.types.target_domain_status.serialize_json(
            value["status"]
        )
    if "verification_status_reason" in value:
        out["verificationStatusReason"] = value["verification_status_reason"]
    return out


def deserialize_json(data: dict) -> VerifyTargetDomainOutput:
    out: VerifyTargetDomainOutput = {}  # type: ignore[typeddict-item]
    if "targetDomainId" in data:
        out["target_domain_id"] = data["targetDomainId"]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "createdAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["created_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["updated_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "verifiedAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["verified_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["verifiedAt"]
            )
        )
    if "status" in data:
        import capo_securityagent.types.target_domain_status

        out["status"] = capo_securityagent.types.target_domain_status.deserialize_json(
            data["status"]
        )
    if "verificationStatusReason" in data:
        out["verification_status_reason"] = data["verificationStatusReason"]
    return out
