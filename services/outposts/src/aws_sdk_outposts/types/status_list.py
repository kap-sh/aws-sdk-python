"""Generated from Smithy shape ``com.amazonaws.outposts#StatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_state

StatusList: TypeAlias = list["aws_sdk_outposts.types.asset_state.AssetState"]


# --- restJson1 ser/de ---
def serialize_json(value: StatusList) -> list:
    import aws_sdk_outposts.types.asset_state

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.asset_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> StatusList:
    import aws_sdk_outposts.types.asset_state

    out: StatusList = []
    for item in data:
        out.append(aws_sdk_outposts.types.asset_state.deserialize_json(item))
    return out
