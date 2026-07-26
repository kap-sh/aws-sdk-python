"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_summary

DatasetSummaries: TypeAlias = list[
    "capo_iotsitewise.types.dataset_summary.DatasetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetSummaries) -> list:
    import capo_iotsitewise.types.dataset_summary

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.dataset_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatasetSummaries:
    import capo_iotsitewise.types.dataset_summary

    out: DatasetSummaries = []
    for item in data:
        out.append(capo_iotsitewise.types.dataset_summary.deserialize_json(item))
    return out
