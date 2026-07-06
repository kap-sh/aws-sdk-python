"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteTargetDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.target_domain_id


class DeleteTargetDomainInput(TypedDict, closed=True):
    target_domain_id: "aws_sdk_securityagent.types.target_domain_id.TargetDomainId"
    """<p>The unique identifier of the target domain to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTargetDomainInput) -> dict:
    out: dict = {}
    out["targetDomainId"] = value["target_domain_id"]
    return out


def deserialize_json(data: dict) -> DeleteTargetDomainInput:
    out: DeleteTargetDomainInput = {}  # type: ignore[typeddict-item]
    if "targetDomainId" in data:
        out["target_domain_id"] = data["targetDomainId"]
    else:
        raise DeserializationError("DeleteTargetDomainInput.target_domain_id required")
    return out
