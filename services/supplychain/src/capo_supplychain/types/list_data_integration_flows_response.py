"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataIntegrationFlowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_list
    import capo_supplychain.types.data_integration_flow_next_token


class ListDataIntegrationFlowsResponse(TypedDict, closed=True):
    flows: "capo_supplychain.types.data_integration_flow_list.DataIntegrationFlowList"
    """<p>The response parameters for ListDataIntegrationFlows.</p>"""
    next_token: NotRequired[
        "capo_supplychain.types.data_integration_flow_next_token.DataIntegrationFlowNextToken"
    ]
    """<p>The pagination token to fetch the next page of the DataIntegrationFlows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationFlowsResponse) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_flow_list

    out["flows"] = capo_supplychain.types.data_integration_flow_list.serialize_json(
        value["flows"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataIntegrationFlowsResponse:
    out: ListDataIntegrationFlowsResponse = {}  # type: ignore[typeddict-item]
    if "flows" in data:
        import capo_supplychain.types.data_integration_flow_list

        out["flows"] = (
            capo_supplychain.types.data_integration_flow_list.deserialize_json(
                data["flows"]
            )
        )
    else:
        raise DeserializationError("ListDataIntegrationFlowsResponse.flows required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
