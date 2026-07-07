"""Generated from Smithy shape ``com.amazonaws.datazone#OverrideDomainUnitOwnersPolicyGrantDetail``."""

from typing_extensions import NotRequired, TypedDict


class OverrideDomainUnitOwnersPolicyGrantDetail(TypedDict, closed=True):
    include_child_domain_units: NotRequired["bool"]
    """<p>Specifies whether the policy is inherited by child domain units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverrideDomainUnitOwnersPolicyGrantDetail) -> dict:
    out: dict = {}
    if "include_child_domain_units" in value:
        out["includeChildDomainUnits"] = value["include_child_domain_units"]
    return out


def deserialize_json(data: dict) -> OverrideDomainUnitOwnersPolicyGrantDetail:
    out: OverrideDomainUnitOwnersPolicyGrantDetail = {}  # type: ignore[typeddict-item]
    if "includeChildDomainUnits" in data:
        out["include_child_domain_units"] = data["includeChildDomainUnits"]
    return out
