"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name

DomainNameList: TypeAlias = list["aws_sdk_opensearch.types.domain_name.DomainName"]


# --- restJson1 ser/de ---
def serialize_json(value: DomainNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> DomainNameList:
    return list(data)
