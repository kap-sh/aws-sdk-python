"""Generated from Smithy shape ``com.amazonaws.odb#DbIormConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.db_iorm_config

DbIormConfigList: TypeAlias = list["aws_sdk_odb.types.db_iorm_config.DbIormConfig"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbIormConfigList) -> list:
    import aws_sdk_odb.types.db_iorm_config

    out: list = []
    for item in value:
        out.append(aws_sdk_odb.types.db_iorm_config.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DbIormConfigList:
    import aws_sdk_odb.types.db_iorm_config

    out: DbIormConfigList = []
    for item in data:
        out.append(aws_sdk_odb.types.db_iorm_config.deserialize_aws_json_1_0(item))
    return out
