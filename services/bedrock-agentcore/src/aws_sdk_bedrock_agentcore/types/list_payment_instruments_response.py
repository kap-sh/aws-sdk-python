"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListPaymentInstrumentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_instrument_summary_list


class ListPaymentInstrumentsResponse(TypedDict):
    payment_instruments: "aws_sdk_bedrock_agentcore.types.payment_instrument_summary_list.PaymentInstrumentSummaryList"
    """<p>List of payment instrument summaries matching the request criteria.</p>"""
    next_token: NotRequired["str"]
    """<p>Token for pagination to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPaymentInstrumentsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.payment_instrument_summary_list

    out["paymentInstruments"] = (
        aws_sdk_bedrock_agentcore.types.payment_instrument_summary_list.serialize_json(
            value["payment_instruments"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPaymentInstrumentsResponse:
    out: ListPaymentInstrumentsResponse = {}  # type: ignore[typeddict-item]
    if "paymentInstruments" in data:
        import aws_sdk_bedrock_agentcore.types.payment_instrument_summary_list

        out["payment_instruments"] = (
            aws_sdk_bedrock_agentcore.types.payment_instrument_summary_list.deserialize_json(
                data["paymentInstruments"]
            )
        )
    else:
        raise DeserializationError(
            "ListPaymentInstrumentsResponse.payment_instruments required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
