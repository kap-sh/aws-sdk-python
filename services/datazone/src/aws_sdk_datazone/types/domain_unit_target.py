"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitTarget``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_unit_id


class DomainUnitTarget(TypedDict):
    domain_unit_id: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the domain unit.</p>"""
    include_child_domain_units: NotRequired["bool"]
    """<p>Specifies whether to apply a rule to the child domain units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitTarget) -> dict:
    out: dict = {}
    out["domainUnitId"] = value["domain_unit_id"]
    if "include_child_domain_units" in value:
        out["includeChildDomainUnits"] = value["include_child_domain_units"]
    return out


def deserialize_json(data: dict) -> DomainUnitTarget:
    out: DomainUnitTarget = {}  # type: ignore[typeddict-item]
    if "domainUnitId" in data:
        out["domain_unit_id"] = data["domainUnitId"]
    else:
        raise DeserializationError("DomainUnitTarget.domain_unit_id required")
    if "includeChildDomainUnits" in data:
        out["include_child_domain_units"] = data["includeChildDomainUnits"]
    return out
