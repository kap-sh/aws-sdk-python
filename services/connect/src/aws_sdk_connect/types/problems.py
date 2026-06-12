"""Generated from Smithy shape ``com.amazonaws.connect#Problems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.problem_detail

Problems: TypeAlias = list["aws_sdk_connect.types.problem_detail.ProblemDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: Problems) -> list:
    import aws_sdk_connect.types.problem_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.problem_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> Problems:
    import aws_sdk_connect.types.problem_detail

    out: Problems = []
    for item in data:
        out.append(aws_sdk_connect.types.problem_detail.deserialize_json(item))
    return out
