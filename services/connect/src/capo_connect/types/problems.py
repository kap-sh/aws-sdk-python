"""Generated from Smithy shape ``com.amazonaws.connect#Problems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.problem_detail

Problems: TypeAlias = list["capo_connect.types.problem_detail.ProblemDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: Problems) -> list:
    import capo_connect.types.problem_detail

    out: list = []
    for item in value:
        out.append(capo_connect.types.problem_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> Problems:
    import capo_connect.types.problem_detail

    out: Problems = []
    for item in data:
        out.append(capo_connect.types.problem_detail.deserialize_json(item))
    return out
