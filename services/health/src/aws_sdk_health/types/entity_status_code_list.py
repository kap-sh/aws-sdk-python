"""Generated from Smithy shape ``com.amazonaws.health#entityStatusCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.entity_status_code

entityStatusCodeList: TypeAlias = list[
    "aws_sdk_health.types.entity_status_code.entityStatusCode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: entityStatusCodeList) -> list:
    import aws_sdk_health.types.entity_status_code

    out: list = []
    for item in value:
        out.append(aws_sdk_health.types.entity_status_code.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> entityStatusCodeList:
    import aws_sdk_health.types.entity_status_code

    out: entityStatusCodeList = []
    for item in data:
        out.append(
            aws_sdk_health.types.entity_status_code.deserialize_aws_json_1_1(item)
        )
    return out
