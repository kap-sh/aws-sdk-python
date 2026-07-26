"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securitylake.types.data_lake_source

DataLakeSourceList: TypeAlias = list[
    "capo_securitylake.types.data_lake_source.DataLakeSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeSourceList) -> list:
    import capo_securitylake.types.data_lake_source

    out: list = []
    for item in value:
        out.append(capo_securitylake.types.data_lake_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataLakeSourceList:
    import capo_securitylake.types.data_lake_source

    out: DataLakeSourceList = []
    for item in data:
        out.append(capo_securitylake.types.data_lake_source.deserialize_json(item))
    return out
