"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#Urns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.urn

Urns: TypeAlias = list["aws_sdk_iotthingsgraph.types.urn.Urn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Urns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Urns:
    return list(data)
