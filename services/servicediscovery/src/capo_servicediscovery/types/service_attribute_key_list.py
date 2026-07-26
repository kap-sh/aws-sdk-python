"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceAttributeKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_servicediscovery.types.service_attribute_key

ServiceAttributeKeyList: TypeAlias = list[
    "capo_servicediscovery.types.service_attribute_key.ServiceAttributeKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceAttributeKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ServiceAttributeKeyList:
    return list(data)
