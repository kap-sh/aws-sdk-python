"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#VpcEndpointFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_status


class VpcEndpointFilters(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_opensearchserverless.types.vpc_endpoint_status.VpcEndpointStatus"
    ]
    """<p>The current status of the endpoint.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointFilters) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcEndpointFilters:
    out: VpcEndpointFilters = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out
