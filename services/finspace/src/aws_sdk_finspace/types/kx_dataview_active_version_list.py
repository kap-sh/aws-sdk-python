"""Generated from Smithy shape ``com.amazonaws.finspace#KxDataviewActiveVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_dataview_active_version

KxDataviewActiveVersionList: TypeAlias = list[
    "aws_sdk_finspace.types.kx_dataview_active_version.KxDataviewActiveVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxDataviewActiveVersionList) -> list:
    import aws_sdk_finspace.types.kx_dataview_active_version

    out: list = []
    for item in value:
        out.append(
            aws_sdk_finspace.types.kx_dataview_active_version.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KxDataviewActiveVersionList:
    import aws_sdk_finspace.types.kx_dataview_active_version

    out: KxDataviewActiveVersionList = []
    for item in data:
        out.append(
            aws_sdk_finspace.types.kx_dataview_active_version.deserialize_json(item)
        )
    return out
