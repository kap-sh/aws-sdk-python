"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ClusterConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ClusterConfiguration(TypedDict):
    ingest_query_instances: NotRequired["int"]
    """<p>The number of instances in the DbCluster which can both ingest and query.</p>"""
    query_only_instances: NotRequired["int"]
    """<p>The number of instances in the DbCluster which can only query.</p>"""
    dedicated_compactor: NotRequired["bool"]
    """<p>Indicates if the compactor instance is a standalone instance or not.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClusterConfiguration) -> dict:
    out: dict = {}
    if "ingest_query_instances" in value:
        out["ingestQueryInstances"] = value["ingest_query_instances"]
    if "query_only_instances" in value:
        out["queryOnlyInstances"] = value["query_only_instances"]
    if "dedicated_compactor" in value:
        out["dedicatedCompactor"] = value["dedicated_compactor"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ClusterConfiguration:
    out: ClusterConfiguration = {}  # type: ignore[typeddict-item]
    if "ingestQueryInstances" in data:
        out["ingest_query_instances"] = data["ingestQueryInstances"]
    if "queryOnlyInstances" in data:
        out["query_only_instances"] = data["queryOnlyInstances"]
    if "dedicatedCompactor" in data:
        out["dedicated_compactor"] = data["dedicatedCompactor"]
    return out
