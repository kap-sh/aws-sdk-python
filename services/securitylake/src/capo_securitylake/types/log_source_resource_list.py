"""Generated from Smithy shape ``com.amazonaws.securitylake#LogSourceResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securitylake.types.log_source_resource

LogSourceResourceList: TypeAlias = list[
    "capo_securitylake.types.log_source_resource.LogSourceResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogSourceResourceList) -> list:
    import capo_securitylake.types.log_source_resource

    out: list = []
    for item in value:
        out.append(capo_securitylake.types.log_source_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogSourceResourceList:
    import capo_securitylake.types.log_source_resource

    out: LogSourceResourceList = []
    for item in data:
        out.append(capo_securitylake.types.log_source_resource.deserialize_json(item))
    return out
