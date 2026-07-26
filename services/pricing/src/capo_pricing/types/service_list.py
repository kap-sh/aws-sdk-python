"""Generated from Smithy shape ``com.amazonaws.pricing#ServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pricing.types.service

ServiceList: TypeAlias = list["capo_pricing.types.service.Service"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceList) -> list:
    import capo_pricing.types.service

    out: list = []
    for item in value:
        out.append(capo_pricing.types.service.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceList:
    import capo_pricing.types.service

    out: ServiceList = []
    for item in data:
        out.append(capo_pricing.types.service.deserialize_aws_json_1_1(item))
    return out
