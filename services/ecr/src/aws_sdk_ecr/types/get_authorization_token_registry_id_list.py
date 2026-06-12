"""Generated from Smithy shape ``com.amazonaws.ecr#GetAuthorizationTokenRegistryIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.registry_id

GetAuthorizationTokenRegistryIdList: TypeAlias = list[
    "aws_sdk_ecr.types.registry_id.RegistryId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAuthorizationTokenRegistryIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GetAuthorizationTokenRegistryIdList:
    return list(data)
