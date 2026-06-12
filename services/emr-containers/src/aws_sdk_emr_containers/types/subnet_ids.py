"""Generated from Smithy shape ``com.amazonaws.emrcontainers#SubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.string256

SubnetIds: TypeAlias = list["aws_sdk_emr_containers.types.string256.String256"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetIds:
    return list(data)
