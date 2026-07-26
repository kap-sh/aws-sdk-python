"""Generated from Smithy shape ``com.amazonaws.configservice#FieldInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.field_info

FieldInfoList: TypeAlias = list["capo_config_service.types.field_info.FieldInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldInfoList) -> list:
    import capo_config_service.types.field_info

    out: list = []
    for item in value:
        out.append(capo_config_service.types.field_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FieldInfoList:
    import capo_config_service.types.field_info

    out: FieldInfoList = []
    for item in data:
        out.append(capo_config_service.types.field_info.deserialize_aws_json_1_1(item))
    return out
