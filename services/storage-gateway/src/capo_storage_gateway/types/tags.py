"""Generated from Smithy shape ``com.amazonaws.storagegateway#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.tag

Tags: TypeAlias = list["capo_storage_gateway.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tags) -> list:
    import capo_storage_gateway.types.tag

    out: list = []
    for item in value:
        out.append(capo_storage_gateway.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Tags:
    import capo_storage_gateway.types.tag

    out: Tags = []
    for item in data:
        out.append(capo_storage_gateway.types.tag.deserialize_aws_json_1_1(item))
    return out
