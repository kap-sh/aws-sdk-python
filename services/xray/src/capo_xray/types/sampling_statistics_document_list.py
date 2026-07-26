"""Generated from Smithy shape ``com.amazonaws.xray#SamplingStatisticsDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.sampling_statistics_document

SamplingStatisticsDocumentList: TypeAlias = list[
    "capo_xray.types.sampling_statistics_document.SamplingStatisticsDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: SamplingStatisticsDocumentList) -> list:
    import capo_xray.types.sampling_statistics_document

    out: list = []
    for item in value:
        out.append(capo_xray.types.sampling_statistics_document.serialize_json(item))
    return out


def deserialize_json(data: list) -> SamplingStatisticsDocumentList:
    import capo_xray.types.sampling_statistics_document

    out: SamplingStatisticsDocumentList = []
    for item in data:
        out.append(capo_xray.types.sampling_statistics_document.deserialize_json(item))
    return out
