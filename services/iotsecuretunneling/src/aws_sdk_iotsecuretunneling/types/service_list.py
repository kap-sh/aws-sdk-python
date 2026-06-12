"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#ServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.service

ServiceList: TypeAlias = list["aws_sdk_iotsecuretunneling.types.service.Service"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ServiceList:
    return list(data)
