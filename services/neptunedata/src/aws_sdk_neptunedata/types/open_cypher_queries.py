"""Generated from Smithy shape ``com.amazonaws.neptunedata#OpenCypherQueries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.gremlin_query_status

OpenCypherQueries: TypeAlias = list[
    "aws_sdk_neptunedata.types.gremlin_query_status.GremlinQueryStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: OpenCypherQueries) -> list:
    import aws_sdk_neptunedata.types.gremlin_query_status

    out: list = []
    for item in value:
        out.append(aws_sdk_neptunedata.types.gremlin_query_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> OpenCypherQueries:
    import aws_sdk_neptunedata.types.gremlin_query_status

    out: OpenCypherQueries = []
    for item in data:
        out.append(
            aws_sdk_neptunedata.types.gremlin_query_status.deserialize_json(item)
        )
    return out
