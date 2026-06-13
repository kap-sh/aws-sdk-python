"""Generated from Smithy shape ``com.amazonaws.datazone#CreateEnvironmentProfilePolicyGrantDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_unit_id


class CreateEnvironmentProfilePolicyGrantDetail(TypedDict):
    domain_unit_id: NotRequired["aws_sdk_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the domain unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentProfilePolicyGrantDetail) -> dict:
    out: dict = {}
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentProfilePolicyGrantDetail:
    out: CreateEnvironmentProfilePolicyGrantDetail = {}  # type: ignore[typeddict-item]
    if "domainUnitId" in data:
        out["domain_unit_id"] = data["domainUnitId"]
    return out
