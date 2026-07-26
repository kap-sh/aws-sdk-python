"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaExecArgsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.lambda_exec_arg

LambdaExecArgsList: TypeAlias = list[
    "capo_greengrassv2.types.lambda_exec_arg.LambdaExecArg"
]


# --- restJson1 ser/de ---
def serialize_json(value: LambdaExecArgsList) -> list:
    return list(value)


def deserialize_json(data: list) -> LambdaExecArgsList:
    return list(data)
