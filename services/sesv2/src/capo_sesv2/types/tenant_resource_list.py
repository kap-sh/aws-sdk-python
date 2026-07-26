"""Generated from Smithy shape ``com.amazonaws.sesv2#TenantResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.tenant_resource

TenantResourceList: TypeAlias = list["capo_sesv2.types.tenant_resource.TenantResource"]


# --- restJson1 ser/de ---
def serialize_json(value: TenantResourceList) -> list:
    import capo_sesv2.types.tenant_resource

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.tenant_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> TenantResourceList:
    import capo_sesv2.types.tenant_resource

    out: TenantResourceList = []
    for item in data:
        out.append(capo_sesv2.types.tenant_resource.deserialize_json(item))
    return out
