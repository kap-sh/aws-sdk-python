"""Generated from Smithy shape ``com.amazonaws.fis#ResolvedTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.resolved_target

ResolvedTargetList: TypeAlias = list["aws_sdk_fis.types.resolved_target.ResolvedTarget"]


# --- restJson1 ser/de ---
def serialize_json(value: ResolvedTargetList) -> list:
    import aws_sdk_fis.types.resolved_target

    out: list = []
    for item in value:
        out.append(aws_sdk_fis.types.resolved_target.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResolvedTargetList:
    import aws_sdk_fis.types.resolved_target

    out: ResolvedTargetList = []
    for item in data:
        out.append(aws_sdk_fis.types.resolved_target.deserialize_json(item))
    return out
