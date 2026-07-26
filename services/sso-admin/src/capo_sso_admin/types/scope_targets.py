"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ScopeTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.scope_target

ScopeTargets: TypeAlias = list["capo_sso_admin.types.scope_target.ScopeTarget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScopeTargets) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ScopeTargets:
    return list(data)
