"""Generated from Smithy shape ``com.amazonaws.xray#SamplingStatisticsDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.sampling_statistics_document

SamplingStatisticsDocumentList: TypeAlias = list[
    "aws_sdk_xray.types.sampling_statistics_document.SamplingStatisticsDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: SamplingStatisticsDocumentList) -> list:
    import aws_sdk_xray.types.sampling_statistics_document

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.sampling_statistics_document.serialize_json(item))
    return out


def deserialize_json(data: list) -> SamplingStatisticsDocumentList:
    import aws_sdk_xray.types.sampling_statistics_document

    out: SamplingStatisticsDocumentList = []
    for item in data:
        out.append(
            aws_sdk_xray.types.sampling_statistics_document.deserialize_json(item)
        )
    return out
