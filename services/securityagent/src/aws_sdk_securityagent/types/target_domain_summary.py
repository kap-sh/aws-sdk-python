"""Generated from Smithy shape ``com.amazonaws.securityagent#TargetDomainSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.target_domain_id
    import aws_sdk_securityagent.types.target_domain_status


class TargetDomainSummary(TypedDict, closed=True):
    target_domain_id: "aws_sdk_securityagent.types.target_domain_id.TargetDomainId"
    """<p>The unique identifier of the target domain.</p>"""
    domain_name: "str"
    """<p>The domain name of the target domain.</p>"""
    verification_status: NotRequired[
        "aws_sdk_securityagent.types.target_domain_status.TargetDomainStatus"
    ]
    """<p>The current verification status of the target domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetDomainSummary) -> dict:
    out: dict = {}
    out["targetDomainId"] = value["target_domain_id"]
    out["domainName"] = value["domain_name"]
    if "verification_status" in value:
        import aws_sdk_securityagent.types.target_domain_status

        out["verificationStatus"] = (
            aws_sdk_securityagent.types.target_domain_status.serialize_json(
                value["verification_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> TargetDomainSummary:
    out: TargetDomainSummary = {}  # type: ignore[typeddict-item]
    if "targetDomainId" in data:
        out["target_domain_id"] = data["targetDomainId"]
    else:
        raise DeserializationError("TargetDomainSummary.target_domain_id required")
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("TargetDomainSummary.domain_name required")
    if "verificationStatus" in data:
        import aws_sdk_securityagent.types.target_domain_status

        out["verification_status"] = (
            aws_sdk_securityagent.types.target_domain_status.deserialize_json(
                data["verificationStatus"]
            )
        )
    return out
