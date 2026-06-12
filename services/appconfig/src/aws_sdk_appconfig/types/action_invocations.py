"""Generated from Smithy shape ``com.amazonaws.appconfig#ActionInvocations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.action_invocation

ActionInvocations: TypeAlias = list[
    "aws_sdk_appconfig.types.action_invocation.ActionInvocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionInvocations) -> list:
    import aws_sdk_appconfig.types.action_invocation

    out: list = []
    for item in value:
        out.append(aws_sdk_appconfig.types.action_invocation.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionInvocations:
    import aws_sdk_appconfig.types.action_invocation

    out: ActionInvocations = []
    for item in data:
        out.append(aws_sdk_appconfig.types.action_invocation.deserialize_json(item))
    return out
