"""Generated from Smithy shape ``com.amazonaws.rum#AppMonitorDomainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rum.types.app_monitor_domain

AppMonitorDomainList: TypeAlias = list[
    "capo_rum.types.app_monitor_domain.AppMonitorDomain"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppMonitorDomainList) -> list:
    return list(value)


def deserialize_json(data: list) -> AppMonitorDomainList:
    return list(data)
