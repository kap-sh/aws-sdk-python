"""Generated from Smithy shape ``com.amazonaws.datazone#OverrideProjectOwnersPolicyGrantDetail``."""

from typing_extensions import NotRequired, TypedDict


class OverrideProjectOwnersPolicyGrantDetail(TypedDict, closed=True):
    include_child_domain_units: NotRequired["bool"]
    """<p>Specifies whether the policy is inherited by child domain units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverrideProjectOwnersPolicyGrantDetail) -> dict:
    out: dict = {}
    if "include_child_domain_units" in value:
        out["includeChildDomainUnits"] = value["include_child_domain_units"]
    return out


def deserialize_json(data: dict) -> OverrideProjectOwnersPolicyGrantDetail:
    out: OverrideProjectOwnersPolicyGrantDetail = {}  # type: ignore[typeddict-item]
    if "includeChildDomainUnits" in data:
        out["include_child_domain_units"] = data["includeChildDomainUnits"]
    return out
