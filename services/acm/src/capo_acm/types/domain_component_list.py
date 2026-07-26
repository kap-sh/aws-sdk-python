"""Generated from Smithy shape ``com.amazonaws.acm#DomainComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.string

DomainComponentList: TypeAlias = list["capo_acm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainComponentList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DomainComponentList:
    return list(data)
