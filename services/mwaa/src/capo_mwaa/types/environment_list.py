"""Generated from Smithy shape ``com.amazonaws.mwaa#EnvironmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa.types.environment_name

EnvironmentList: TypeAlias = list["capo_mwaa.types.environment_name.EnvironmentName"]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentList) -> list:
    return list(value)


def deserialize_json(data: list) -> EnvironmentList:
    return list(data)
