"""Generated from Smithy shape ``com.amazonaws.lakeformation#ScopeTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.scope_target

ScopeTargets: TypeAlias = list["aws_sdk_lakeformation.types.scope_target.ScopeTarget"]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeTargets) -> list:
    return list(value)


def deserialize_json(data: list) -> ScopeTargets:
    return list(data)
