"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixRow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_matrix_entry

RouteMatrixRow: TypeAlias = list[
    "capo_geo_routes.types.route_matrix_entry.RouteMatrixEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixRow) -> list:
    import capo_geo_routes.types.route_matrix_entry

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_matrix_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteMatrixRow:
    import capo_geo_routes.types.route_matrix_entry

    out: RouteMatrixRow = []
    for item in data:
        out.append(capo_geo_routes.types.route_matrix_entry.deserialize_json(item))
    return out
