"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265WriteMp4PackagingType``."""

from typing import Literal, TypeAlias, cast

"""If the location of parameter set NAL units doesn't matter in your workflow, ignore this setting. Use this setting only with CMAF or DASH outputs, or with standalone file outputs in an MPEG-4 container (MP4 outputs). Choose HVC1 to mark your output as HVC1. This makes your output compliant with the following specification: ISO IECJTC1 SC29 N13798 Text ISO/IEC FDIS 14496-15 3rd Edition. For these outputs, the service stores parameter set NAL units in the sample headers but not in the samples directly. For MP4 outputs, when you choose HVC1, your output video might not work properly with some downstream systems and video players. The service defaults to marking your output as HEV1. For these outputs, the service writes parameter set NAL units directly into the samples."""
H265WriteMp4PackagingType: TypeAlias = Literal[
    "HVC1",
    "HEV1",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265WriteMp4PackagingType) -> str:
    return value


def deserialize_json(data: str) -> H265WriteMp4PackagingType:
    return cast(H265WriteMp4PackagingType, data)
