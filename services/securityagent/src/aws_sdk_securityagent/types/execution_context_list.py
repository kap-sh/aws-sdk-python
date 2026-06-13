"""Generated from Smithy shape ``com.amazonaws.securityagent#ExecutionContextList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.execution_context

ExecutionContextList: TypeAlias = list[
    "aws_sdk_securityagent.types.execution_context.ExecutionContext"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionContextList) -> list:
    import aws_sdk_securityagent.types.execution_context

    out: list = []
    for item in value:
        out.append(aws_sdk_securityagent.types.execution_context.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExecutionContextList:
    import aws_sdk_securityagent.types.execution_context

    out: ExecutionContextList = []
    for item in data:
        out.append(aws_sdk_securityagent.types.execution_context.deserialize_json(item))
    return out
