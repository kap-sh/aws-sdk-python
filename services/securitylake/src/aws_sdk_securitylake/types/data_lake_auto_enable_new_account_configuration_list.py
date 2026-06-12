"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeAutoEnableNewAccountConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_auto_enable_new_account_configuration

DataLakeAutoEnableNewAccountConfigurationList: TypeAlias = list["aws_sdk_securitylake.types.data_lake_auto_enable_new_account_configuration.DataLakeAutoEnableNewAccountConfiguration"]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeAutoEnableNewAccountConfigurationList) -> list:
    import aws_sdk_securitylake.types.data_lake_auto_enable_new_account_configuration
    out: list = []
    for item in value:
        out.append(aws_sdk_securitylake.types.data_lake_auto_enable_new_account_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataLakeAutoEnableNewAccountConfigurationList:
    import aws_sdk_securitylake.types.data_lake_auto_enable_new_account_configuration
    out: DataLakeAutoEnableNewAccountConfigurationList = []
    for item in data:
        out.append(aws_sdk_securitylake.types.data_lake_auto_enable_new_account_configuration.deserialize_json(item))
    return out