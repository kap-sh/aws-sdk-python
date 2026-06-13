"""Generated from Smithy shape ``com.amazonaws.qconnect#Citations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.citation

Citations: TypeAlias = list["aws_sdk_qconnect.types.citation.Citation"]


# --- restJson1 ser/de ---
def serialize_json(value: Citations) -> list:
    import aws_sdk_qconnect.types.citation

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.citation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Citations:
    import aws_sdk_qconnect.types.citation

    out: Citations = []
    for item in data:
        out.append(aws_sdk_qconnect.types.citation.deserialize_json(item))
    return out
