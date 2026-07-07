"""Generated from Smithy shape ``com.amazonaws.datazone#CreateFormTypePolicyGrantDetail``."""

from typing_extensions import NotRequired, TypedDict


class CreateFormTypePolicyGrantDetail(TypedDict, closed=True):
    include_child_domain_units: NotRequired["bool"]
    """<p>Specifies whether the policy grant is applied to child domain units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFormTypePolicyGrantDetail) -> dict:
    out: dict = {}
    if "include_child_domain_units" in value:
        out["includeChildDomainUnits"] = value["include_child_domain_units"]
    return out


def deserialize_json(data: dict) -> CreateFormTypePolicyGrantDetail:
    out: CreateFormTypePolicyGrantDetail = {}  # type: ignore[typeddict-item]
    if "includeChildDomainUnits" in data:
        out["include_child_domain_units"] = data["includeChildDomainUnits"]
    return out
