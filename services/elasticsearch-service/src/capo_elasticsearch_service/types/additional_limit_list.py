"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AdditionalLimitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.additional_limit

AdditionalLimitList: TypeAlias = list[
    "capo_elasticsearch_service.types.additional_limit.AdditionalLimit"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalLimitList) -> list:
    import capo_elasticsearch_service.types.additional_limit

    out: list = []
    for item in value:
        out.append(
            capo_elasticsearch_service.types.additional_limit.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AdditionalLimitList:
    import capo_elasticsearch_service.types.additional_limit

    out: AdditionalLimitList = []
    for item in data:
        out.append(
            capo_elasticsearch_service.types.additional_limit.deserialize_json(item)
        )
    return out
