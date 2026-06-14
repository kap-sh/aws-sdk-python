"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftClusterStorage``."""

from typing import TypedDict

from aws_sdk_datazone.errors import DeserializationError


class RedshiftClusterStorage(TypedDict):
    cluster_name: "str"
    """<p>The name of an Amazon Redshift cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftClusterStorage) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
    return out


def deserialize_json(data: dict) -> RedshiftClusterStorage:
    out: RedshiftClusterStorage = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    else:
        raise DeserializationError("RedshiftClusterStorage.cluster_name required")
    return out
