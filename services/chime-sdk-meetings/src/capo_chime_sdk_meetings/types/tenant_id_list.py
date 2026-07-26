"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TenantIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.tenant_id

TenantIdList: TypeAlias = list["capo_chime_sdk_meetings.types.tenant_id.TenantId"]


# --- restJson1 ser/de ---
def serialize_json(value: TenantIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> TenantIdList:
    return list(data)
