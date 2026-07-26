"""Generated from Smithy shape ``com.amazonaws.batch#ListJobsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.key_values_pair

ListJobsFilterList: TypeAlias = list["capo_batch.types.key_values_pair.KeyValuesPair"]


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsFilterList) -> list:
    import capo_batch.types.key_values_pair

    out: list = []
    for item in value:
        out.append(capo_batch.types.key_values_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListJobsFilterList:
    import capo_batch.types.key_values_pair

    out: ListJobsFilterList = []
    for item in data:
        out.append(capo_batch.types.key_values_pair.deserialize_json(item))
    return out
