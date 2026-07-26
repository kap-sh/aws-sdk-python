"""Generated from Smithy shape ``com.amazonaws.xray#SamplingTargetDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.sampling_target_document

SamplingTargetDocumentList: TypeAlias = list[
    "capo_xray.types.sampling_target_document.SamplingTargetDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: SamplingTargetDocumentList) -> list:
    import capo_xray.types.sampling_target_document

    out: list = []
    for item in value:
        out.append(capo_xray.types.sampling_target_document.serialize_json(item))
    return out


def deserialize_json(data: list) -> SamplingTargetDocumentList:
    import capo_xray.types.sampling_target_document

    out: SamplingTargetDocumentList = []
    for item in data:
        out.append(capo_xray.types.sampling_target_document.deserialize_json(item))
    return out
