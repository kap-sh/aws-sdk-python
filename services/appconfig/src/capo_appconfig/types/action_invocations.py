"""Generated from Smithy shape ``com.amazonaws.appconfig#ActionInvocations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.action_invocation

ActionInvocations: TypeAlias = list[
    "capo_appconfig.types.action_invocation.ActionInvocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionInvocations) -> list:
    import capo_appconfig.types.action_invocation

    out: list = []
    for item in value:
        out.append(capo_appconfig.types.action_invocation.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionInvocations:
    import capo_appconfig.types.action_invocation

    out: ActionInvocations = []
    for item in data:
        out.append(capo_appconfig.types.action_invocation.deserialize_json(item))
    return out
