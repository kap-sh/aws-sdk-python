"""Generated from Smithy shape ``com.amazonaws.xray#SamplingBoostStatisticsDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.sampling_boost_statistics_document

SamplingBoostStatisticsDocumentList: TypeAlias = list[
    "aws_sdk_xray.types.sampling_boost_statistics_document.SamplingBoostStatisticsDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: SamplingBoostStatisticsDocumentList) -> list:
    import aws_sdk_xray.types.sampling_boost_statistics_document

    out: list = []
    for item in value:
        out.append(
            aws_sdk_xray.types.sampling_boost_statistics_document.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SamplingBoostStatisticsDocumentList:
    import aws_sdk_xray.types.sampling_boost_statistics_document

    out: SamplingBoostStatisticsDocumentList = []
    for item in data:
        out.append(
            aws_sdk_xray.types.sampling_boost_statistics_document.deserialize_json(item)
        )
    return out
