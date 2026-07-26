"""Generated from Smithy shape ``com.amazonaws.neptunedata#GremlinQueries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_neptunedata.types.gremlin_query_status

GremlinQueries: TypeAlias = list[
    "capo_neptunedata.types.gremlin_query_status.GremlinQueryStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: GremlinQueries) -> list:
    import capo_neptunedata.types.gremlin_query_status

    out: list = []
    for item in value:
        out.append(capo_neptunedata.types.gremlin_query_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> GremlinQueries:
    import capo_neptunedata.types.gremlin_query_status

    out: GremlinQueries = []
    for item in data:
        out.append(capo_neptunedata.types.gremlin_query_status.deserialize_json(item))
    return out
