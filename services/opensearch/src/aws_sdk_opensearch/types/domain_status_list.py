"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_status

DomainStatusList: TypeAlias = list[
    "aws_sdk_opensearch.types.domain_status.DomainStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainStatusList) -> list:
    import aws_sdk_opensearch.types.domain_status

    out: list = []
    for item in value:
        out.append(aws_sdk_opensearch.types.domain_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainStatusList:
    import aws_sdk_opensearch.types.domain_status

    out: DomainStatusList = []
    for item in data:
        out.append(aws_sdk_opensearch.types.domain_status.deserialize_json(item))
    return out
