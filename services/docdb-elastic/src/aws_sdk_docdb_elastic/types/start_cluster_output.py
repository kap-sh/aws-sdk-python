"""Generated from Smithy shape ``com.amazonaws.docdbelastic#StartClusterOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.cluster


class StartClusterOutput(TypedDict):
    cluster: "aws_sdk_docdb_elastic.types.cluster.Cluster"


# --- restJson1 ser/de ---
def serialize_json(value: StartClusterOutput) -> dict:
    out: dict = {}
    import aws_sdk_docdb_elastic.types.cluster

    out["cluster"] = aws_sdk_docdb_elastic.types.cluster.serialize_json(
        value["cluster"]
    )
    return out


def deserialize_json(data: dict) -> StartClusterOutput:
    out: StartClusterOutput = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import aws_sdk_docdb_elastic.types.cluster

        out["cluster"] = aws_sdk_docdb_elastic.types.cluster.deserialize_json(
            data["cluster"]
        )
    else:
        raise DeserializationError("StartClusterOutput.cluster required")
    return out
