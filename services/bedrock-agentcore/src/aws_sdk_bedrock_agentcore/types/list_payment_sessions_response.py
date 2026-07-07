"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListPaymentSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.next_token
    import aws_sdk_bedrock_agentcore.types.payment_session_summary_list


class ListPaymentSessionsResponse(TypedDict, closed=True):
    payment_sessions: "aws_sdk_bedrock_agentcore.types.payment_session_summary_list.PaymentSessionSummaryList"
    """<p>List of payment session summaries matching the request criteria.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agentcore.types.next_token.NextToken"]
    """<p>Token for pagination to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPaymentSessionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.payment_session_summary_list

    out["paymentSessions"] = (
        aws_sdk_bedrock_agentcore.types.payment_session_summary_list.serialize_json(
            value["payment_sessions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPaymentSessionsResponse:
    out: ListPaymentSessionsResponse = {}  # type: ignore[typeddict-item]
    if "paymentSessions" in data:
        import aws_sdk_bedrock_agentcore.types.payment_session_summary_list

        out["payment_sessions"] = (
            aws_sdk_bedrock_agentcore.types.payment_session_summary_list.deserialize_json(
                data["paymentSessions"]
            )
        )
    else:
        raise DeserializationError(
            "ListPaymentSessionsResponse.payment_sessions required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
