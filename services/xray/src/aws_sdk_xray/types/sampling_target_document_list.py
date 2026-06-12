"""Generated from Smithy shape ``com.amazonaws.xray#SamplingTargetDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.sampling_target_document

SamplingTargetDocumentList: TypeAlias = list[
    "aws_sdk_xray.types.sampling_target_document.SamplingTargetDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: SamplingTargetDocumentList) -> list:
    import aws_sdk_xray.types.sampling_target_document

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.sampling_target_document.serialize_json(item))
    return out


def deserialize_json(data: list) -> SamplingTargetDocumentList:
    import aws_sdk_xray.types.sampling_target_document

    out: SamplingTargetDocumentList = []
    for item in data:
        out.append(aws_sdk_xray.types.sampling_target_document.deserialize_json(item))
    return out
