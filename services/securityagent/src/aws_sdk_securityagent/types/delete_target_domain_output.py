"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteTargetDomainOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.target_domain_id


class DeleteTargetDomainOutput(TypedDict):
    target_domain_id: NotRequired[
        "aws_sdk_securityagent.types.target_domain_id.TargetDomainId"
    ]
    """<p>The unique identifier of the deleted target domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTargetDomainOutput) -> dict:
    out: dict = {}
    if "target_domain_id" in value:
        out["targetDomainId"] = value["target_domain_id"]
    return out


def deserialize_json(data: dict) -> DeleteTargetDomainOutput:
    out: DeleteTargetDomainOutput = {}  # type: ignore[typeddict-item]
    if "targetDomainId" in data:
        out["target_domain_id"] = data["targetDomainId"]
    return out
