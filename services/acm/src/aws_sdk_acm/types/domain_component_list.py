"""Generated from Smithy shape ``com.amazonaws.acm#DomainComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm.types.string

DomainComponentList: TypeAlias = list["aws_sdk_acm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainComponentList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DomainComponentList:
    return list(data)
