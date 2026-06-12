"""Generated from Smithy shape ``com.amazonaws.ecrpublic#OperatingSystemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.operating_system

OperatingSystemList: TypeAlias = list[
    "aws_sdk_ecr_public.types.operating_system.OperatingSystem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperatingSystemList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OperatingSystemList:
    return list(data)
