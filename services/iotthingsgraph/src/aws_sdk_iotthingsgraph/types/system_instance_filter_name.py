"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemInstanceFilterName``."""

from typing import Literal, TypeAlias, cast

SystemInstanceFilterName: TypeAlias = Literal[
    "SYSTEM_TEMPLATE_ID",
    "STATUS",
    "GREENGRASS_GROUP_NAME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemInstanceFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SystemInstanceFilterName:
    return cast(SystemInstanceFilterName, data)
