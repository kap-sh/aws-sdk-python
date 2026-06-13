"""Generated from Smithy shape ``com.amazonaws.location#RouteMatrixRow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.route_matrix_entry

RouteMatrixRow: TypeAlias = list[
    "aws_sdk_location.types.route_matrix_entry.RouteMatrixEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixRow) -> list:
    import aws_sdk_location.types.route_matrix_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.route_matrix_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteMatrixRow:
    import aws_sdk_location.types.route_matrix_entry

    out: RouteMatrixRow = []
    for item in data:
        out.append(aws_sdk_location.types.route_matrix_entry.deserialize_json(item))
    return out
