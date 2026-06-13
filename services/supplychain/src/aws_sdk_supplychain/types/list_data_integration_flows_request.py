"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataIntegrationFlowsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_max_results
    import aws_sdk_supplychain.types.data_integration_flow_next_token
    import aws_sdk_supplychain.types.uuid


class ListDataIntegrationFlowsRequest(TypedDict):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    next_token: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_next_token.DataIntegrationFlowNextToken"
    ]
    """<p>The pagination token to fetch the next page of the DataIntegrationFlows.</p>"""
    max_results: "aws_sdk_supplychain.types.data_integration_flow_max_results.DataIntegrationFlowMaxResults"
    """<p>Specify the maximum number of DataIntegrationFlows to fetch in one paginated request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationFlowsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataIntegrationFlowsRequest:
    out: ListDataIntegrationFlowsRequest = {}  # type: ignore[typeddict-item]
    return out
