"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#LimitValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.limit_value

LimitValueList: TypeAlias = list[
    "capo_elasticsearch_service.types.limit_value.LimitValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: LimitValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> LimitValueList:
    return list(data)
