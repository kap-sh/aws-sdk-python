"""Generated from Smithy shape ``com.amazonaws.sesv2#TenantInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.tenant_info

TenantInfoList: TypeAlias = list["aws_sdk_sesv2.types.tenant_info.TenantInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: TenantInfoList) -> list:
    import aws_sdk_sesv2.types.tenant_info

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.tenant_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> TenantInfoList:
    import aws_sdk_sesv2.types.tenant_info

    out: TenantInfoList = []
    for item in data:
        out.append(aws_sdk_sesv2.types.tenant_info.deserialize_json(item))
    return out
