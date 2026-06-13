"""Generated from Smithy shape ``com.amazonaws.datazone#CreateGlossaryPolicyGrantDetail``."""

from typing import TypedDict
from typing_extensions import NotRequired


class CreateGlossaryPolicyGrantDetail(TypedDict):
    include_child_domain_units: NotRequired["bool"]
    """<p>Specifies whether the policy grant is applied to child domain units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGlossaryPolicyGrantDetail) -> dict:
    out: dict = {}
    if "include_child_domain_units" in value:
        out["includeChildDomainUnits"] = value["include_child_domain_units"]
    return out


def deserialize_json(data: dict) -> CreateGlossaryPolicyGrantDetail:
    out: CreateGlossaryPolicyGrantDetail = {}  # type: ignore[typeddict-item]
    if "includeChildDomainUnits" in data:
        out["include_child_domain_units"] = data["includeChildDomainUnits"]
    return out
