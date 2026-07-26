"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeSourceStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securitylake.types.data_lake_source_status

DataLakeSourceStatusList: TypeAlias = list[
    "capo_securitylake.types.data_lake_source_status.DataLakeSourceStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeSourceStatusList) -> list:
    import capo_securitylake.types.data_lake_source_status

    out: list = []
    for item in value:
        out.append(capo_securitylake.types.data_lake_source_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataLakeSourceStatusList:
    import capo_securitylake.types.data_lake_source_status

    out: DataLakeSourceStatusList = []
    for item in data:
        out.append(
            capo_securitylake.types.data_lake_source_status.deserialize_json(item)
        )
    return out
