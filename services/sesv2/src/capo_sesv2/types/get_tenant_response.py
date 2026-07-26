"""Generated from Smithy shape ``com.amazonaws.sesv2#GetTenantResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.tenant


class GetTenantResponse(TypedDict, closed=True):
    tenant: NotRequired["capo_sesv2.types.tenant.Tenant"]
    """<p>A structure that contains details about the tenant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTenantResponse) -> dict:
    out: dict = {}
    if "tenant" in value:
        import capo_sesv2.types.tenant

        out["Tenant"] = capo_sesv2.types.tenant.serialize_json(value["tenant"])
    return out


def deserialize_json(data: dict) -> GetTenantResponse:
    out: GetTenantResponse = {}  # type: ignore[typeddict-item]
    if "Tenant" in data:
        import capo_sesv2.types.tenant

        out["tenant"] = capo_sesv2.types.tenant.deserialize_json(data["Tenant"])
    return out
