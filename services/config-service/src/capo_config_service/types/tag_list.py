"""Generated from Smithy shape ``com.amazonaws.configservice#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.tag

TagList: TypeAlias = list["capo_config_service.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagList) -> list:
    import capo_config_service.types.tag

    out: list = []
    for item in value:
        out.append(capo_config_service.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TagList:
    import capo_config_service.types.tag

    out: TagList = []
    for item in data:
        out.append(capo_config_service.types.tag.deserialize_aws_json_1_1(item))
    return out
