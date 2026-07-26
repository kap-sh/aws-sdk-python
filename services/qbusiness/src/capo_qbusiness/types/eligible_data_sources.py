"""Generated from Smithy shape ``com.amazonaws.qbusiness#EligibleDataSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.eligible_data_source

EligibleDataSources: TypeAlias = list[
    "capo_qbusiness.types.eligible_data_source.EligibleDataSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: EligibleDataSources) -> list:
    import capo_qbusiness.types.eligible_data_source

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.eligible_data_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> EligibleDataSources:
    import capo_qbusiness.types.eligible_data_source

    out: EligibleDataSources = []
    for item in data:
        out.append(capo_qbusiness.types.eligible_data_source.deserialize_json(item))
    return out
