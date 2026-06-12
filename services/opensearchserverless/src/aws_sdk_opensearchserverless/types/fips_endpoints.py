"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#FipsEndpoints``."""

from typing import TypedDict

from typing_extensions import NotRequired


class FipsEndpoints(TypedDict):
    collection_endpoint: NotRequired["str"]
    """<p>FIPS-compliant collection endpoint used to submit index, search, and data upload requests to an OpenSearch Serverless collection. This endpoint uses FIPS 140-3 validated cryptography and is required for federal government workloads.</p>"""
    dashboard_endpoint: NotRequired["str"]
    """<p>FIPS-compliant endpoint used to access OpenSearch Dashboards. This endpoint uses FIPS 140-3 validated cryptography and is required for federal government workloads that need dashboard visualization capabilities.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FipsEndpoints) -> dict:
    out: dict = {}
    if "collection_endpoint" in value:
        out["collectionEndpoint"] = value["collection_endpoint"]
    if "dashboard_endpoint" in value:
        out["dashboardEndpoint"] = value["dashboard_endpoint"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FipsEndpoints:
    out: FipsEndpoints = {}  # type: ignore[typeddict-item]
    if "collectionEndpoint" in data:
        out["collection_endpoint"] = data["collectionEndpoint"]
    if "dashboardEndpoint" in data:
        out["dashboard_endpoint"] = data["dashboardEndpoint"]
    return out
