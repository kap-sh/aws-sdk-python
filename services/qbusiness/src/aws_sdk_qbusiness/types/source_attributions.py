"""Generated from Smithy shape ``com.amazonaws.qbusiness#SourceAttributions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.source_attribution

SourceAttributions: TypeAlias = list[
    "aws_sdk_qbusiness.types.source_attribution.SourceAttribution | None"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceAttributions) -> list:
    import aws_sdk_qbusiness.types.source_attribution

    out: list = []
    for item in value:
        if item is None:
            out.append(None)
            continue
        out.append(aws_sdk_qbusiness.types.source_attribution.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceAttributions:
    import aws_sdk_qbusiness.types.source_attribution

    out: SourceAttributions = []
    for item in data:
        if item is None:
            out.append(None)
            continue
        out.append(aws_sdk_qbusiness.types.source_attribution.deserialize_json(item))
    return out
