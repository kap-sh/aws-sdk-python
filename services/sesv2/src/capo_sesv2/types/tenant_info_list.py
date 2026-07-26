"""Generated from Smithy shape ``com.amazonaws.sesv2#TenantInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.tenant_info

TenantInfoList: TypeAlias = list["capo_sesv2.types.tenant_info.TenantInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: TenantInfoList) -> list:
    import capo_sesv2.types.tenant_info

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.tenant_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> TenantInfoList:
    import capo_sesv2.types.tenant_info

    out: TenantInfoList = []
    for item in data:
        out.append(capo_sesv2.types.tenant_info.deserialize_json(item))
    return out
