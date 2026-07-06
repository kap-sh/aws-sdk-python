"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteTenantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.tenant_name


class DeleteTenantRequest(TypedDict, closed=True):
    tenant_name: "aws_sdk_sesv2.types.tenant_name.TenantName"
    """<p>The name of the tenant to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTenantRequest) -> dict:
    out: dict = {}
    out["TenantName"] = value["tenant_name"]
    return out


def deserialize_json(data: dict) -> DeleteTenantRequest:
    out: DeleteTenantRequest = {}  # type: ignore[typeddict-item]
    if "TenantName" in data:
        out["tenant_name"] = data["TenantName"]
    else:
        raise DeserializationError("DeleteTenantRequest.tenant_name required")
    return out
