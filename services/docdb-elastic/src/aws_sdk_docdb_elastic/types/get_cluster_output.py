"""Generated from Smithy shape ``com.amazonaws.docdbelastic#GetClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.cluster


class GetClusterOutput(TypedDict, closed=True):
    cluster: "aws_sdk_docdb_elastic.types.cluster.Cluster"
    """<p>Returns information about a specific elastic cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClusterOutput) -> dict:
    out: dict = {}
    import aws_sdk_docdb_elastic.types.cluster

    out["cluster"] = aws_sdk_docdb_elastic.types.cluster.serialize_json(
        value["cluster"]
    )
    return out


def deserialize_json(data: dict) -> GetClusterOutput:
    out: GetClusterOutput = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import aws_sdk_docdb_elastic.types.cluster

        out["cluster"] = aws_sdk_docdb_elastic.types.cluster.deserialize_json(
            data["cluster"]
        )
    else:
        raise DeserializationError("GetClusterOutput.cluster required")
    return out
