"""Generated from Smithy shape ``com.amazonaws.inspector#ScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.scope

ScopeList: TypeAlias = list["capo_inspector.types.scope.Scope"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScopeList) -> list:
    import capo_inspector.types.scope

    out: list = []
    for item in value:
        out.append(capo_inspector.types.scope.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ScopeList:
    import capo_inspector.types.scope

    out: ScopeList = []
    for item in data:
        out.append(capo_inspector.types.scope.deserialize_aws_json_1_1(item))
    return out
