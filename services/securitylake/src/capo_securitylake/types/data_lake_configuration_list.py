"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securitylake.types.data_lake_configuration

DataLakeConfigurationList: TypeAlias = list[
    "capo_securitylake.types.data_lake_configuration.DataLakeConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeConfigurationList) -> list:
    import capo_securitylake.types.data_lake_configuration

    out: list = []
    for item in value:
        out.append(capo_securitylake.types.data_lake_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataLakeConfigurationList:
    import capo_securitylake.types.data_lake_configuration

    out: DataLakeConfigurationList = []
    for item in data:
        out.append(
            capo_securitylake.types.data_lake_configuration.deserialize_json(item)
        )
    return out
