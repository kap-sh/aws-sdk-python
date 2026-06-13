"""Generated from Smithy shape ``com.amazonaws.securityagent#VerifyTargetDomainInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.target_domain_id


class VerifyTargetDomainInput(TypedDict):
    target_domain_id: "aws_sdk_securityagent.types.target_domain_id.TargetDomainId"
    """<p>The unique identifier of the target domain to verify.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyTargetDomainInput) -> dict:
    out: dict = {}
    out["targetDomainId"] = value["target_domain_id"]
    return out


def deserialize_json(data: dict) -> VerifyTargetDomainInput:
    out: VerifyTargetDomainInput = {}  # type: ignore[typeddict-item]
    if "targetDomainId" in data:
        out["target_domain_id"] = data["targetDomainId"]
    else:
        raise DeserializationError("VerifyTargetDomainInput.target_domain_id required")
    return out
