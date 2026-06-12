"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DomainInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_info

DomainInfoList: TypeAlias = list[
    "aws_sdk_elasticsearch_service.types.domain_info.DomainInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainInfoList) -> list:
    import aws_sdk_elasticsearch_service.types.domain_info

    out: list = []
    for item in value:
        out.append(aws_sdk_elasticsearch_service.types.domain_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainInfoList:
    import aws_sdk_elasticsearch_service.types.domain_info

    out: DomainInfoList = []
    for item in data:
        out.append(
            aws_sdk_elasticsearch_service.types.domain_info.deserialize_json(item)
        )
    return out
