"""Generated from Smithy shape ``com.amazonaws.neptunegraph#SubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.subnet_id

SubnetIds: TypeAlias = list["aws_sdk_neptune_graph.types.subnet_id.SubnetId"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetIds:
    return list(data)
