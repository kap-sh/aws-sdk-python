"""Generated from Smithy shape ``com.amazonaws.sesv2#GetTenantResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.tenant


class GetTenantResponse(TypedDict):
    tenant: NotRequired["aws_sdk_sesv2.types.tenant.Tenant"]
    """<p>A structure that contains details about the tenant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTenantResponse) -> dict:
    out: dict = {}
    if "tenant" in value:
        import aws_sdk_sesv2.types.tenant

        out["Tenant"] = aws_sdk_sesv2.types.tenant.serialize_json(value["tenant"])
    return out


def deserialize_json(data: dict) -> GetTenantResponse:
    out: GetTenantResponse = {}  # type: ignore[typeddict-item]
    if "Tenant" in data:
        import aws_sdk_sesv2.types.tenant

        out["tenant"] = aws_sdk_sesv2.types.tenant.deserialize_json(data["Tenant"])
    return out
