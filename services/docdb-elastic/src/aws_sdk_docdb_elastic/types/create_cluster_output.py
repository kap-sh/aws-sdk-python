"""Generated from Smithy shape ``com.amazonaws.docdbelastic#CreateClusterOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.cluster


class CreateClusterOutput(TypedDict):
    cluster: "aws_sdk_docdb_elastic.types.cluster.Cluster"
    """<p>The new elastic cluster that has been created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClusterOutput) -> dict:
    out: dict = {}
    import aws_sdk_docdb_elastic.types.cluster

    out["cluster"] = aws_sdk_docdb_elastic.types.cluster.serialize_json(
        value["cluster"]
    )
    return out


def deserialize_json(data: dict) -> CreateClusterOutput:
    out: CreateClusterOutput = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import aws_sdk_docdb_elastic.types.cluster

        out["cluster"] = aws_sdk_docdb_elastic.types.cluster.deserialize_json(
            data["cluster"]
        )
    else:
        raise DeserializationError("CreateClusterOutput.cluster required")
    return out
