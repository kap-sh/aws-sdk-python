"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeAutoEnableNewAccountConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securitylake.types.data_lake_auto_enable_new_account_configuration

DataLakeAutoEnableNewAccountConfigurationList: TypeAlias = list[
    "capo_securitylake.types.data_lake_auto_enable_new_account_configuration.DataLakeAutoEnableNewAccountConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeAutoEnableNewAccountConfigurationList) -> list:
    import capo_securitylake.types.data_lake_auto_enable_new_account_configuration

    out: list = []
    for item in value:
        out.append(
            capo_securitylake.types.data_lake_auto_enable_new_account_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataLakeAutoEnableNewAccountConfigurationList:
    import capo_securitylake.types.data_lake_auto_enable_new_account_configuration

    out: DataLakeAutoEnableNewAccountConfigurationList = []
    for item in data:
        out.append(
            capo_securitylake.types.data_lake_auto_enable_new_account_configuration.deserialize_json(
                item
            )
        )
    return out
