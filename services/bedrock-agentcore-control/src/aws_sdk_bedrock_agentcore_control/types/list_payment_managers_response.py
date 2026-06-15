"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPaymentManagersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_summaries


class ListPaymentManagersResponse(TypedDict):
    payment_managers: "aws_sdk_bedrock_agentcore_control.types.payment_manager_summaries.PaymentManagerSummaries"
    """<p>The list of payment manager summaries. For details about the fields in each summary, see the <code>PaymentManagerSummary</code> data type.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPaymentManagersResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_summaries

    out["paymentManagers"] = (
        aws_sdk_bedrock_agentcore_control.types.payment_manager_summaries.serialize_json(
            value["payment_managers"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPaymentManagersResponse:
    out: ListPaymentManagersResponse = {}  # type: ignore[typeddict-item]
    if "paymentManagers" in data:
        import aws_sdk_bedrock_agentcore_control.types.payment_manager_summaries

        out["payment_managers"] = (
            aws_sdk_bedrock_agentcore_control.types.payment_manager_summaries.deserialize_json(
                data["paymentManagers"]
            )
        )
    else:
        raise DeserializationError(
            "ListPaymentManagersResponse.payment_managers required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
