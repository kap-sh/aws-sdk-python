"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataIntegrationFlowExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_execution_list
    import aws_sdk_supplychain.types.data_integration_flow_execution_next_token


class ListDataIntegrationFlowExecutionsResponse(TypedDict, closed=True):
    flow_executions: "aws_sdk_supplychain.types.data_integration_flow_execution_list.DataIntegrationFlowExecutionList"
    """<p>The list of flow executions.</p>"""
    next_token: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_execution_next_token.DataIntegrationFlowExecutionNextToken"
    ]
    """<p>The pagination token to fetch next page of flow executions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationFlowExecutionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_integration_flow_execution_list

    out["flowExecutions"] = (
        aws_sdk_supplychain.types.data_integration_flow_execution_list.serialize_json(
            value["flow_executions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataIntegrationFlowExecutionsResponse:
    out: ListDataIntegrationFlowExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "flowExecutions" in data:
        import aws_sdk_supplychain.types.data_integration_flow_execution_list

        out["flow_executions"] = (
            aws_sdk_supplychain.types.data_integration_flow_execution_list.deserialize_json(
                data["flowExecutions"]
            )
        )
    else:
        raise DeserializationError(
            "ListDataIntegrationFlowExecutionsResponse.flow_executions required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
