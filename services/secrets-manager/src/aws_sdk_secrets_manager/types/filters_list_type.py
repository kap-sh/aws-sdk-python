"""Generated from Smithy shape ``com.amazonaws.secretsmanager#FiltersListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.filter

FiltersListType: TypeAlias = list["aws_sdk_secrets_manager.types.filter.Filter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FiltersListType) -> list:
    import aws_sdk_secrets_manager.types.filter

    out: list = []
    for item in value:
        out.append(aws_sdk_secrets_manager.types.filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FiltersListType:
    import aws_sdk_secrets_manager.types.filter

    out: FiltersListType = []
    for item in data:
        out.append(aws_sdk_secrets_manager.types.filter.deserialize_aws_json_1_1(item))
    return out
