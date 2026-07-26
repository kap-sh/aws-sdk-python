"""Generated from Smithy shape ``com.amazonaws.kinesis#ListStreamConsumersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.consumer_list
    import capo_kinesis.types.next_token


class ListStreamConsumersOutput(TypedDict, closed=True):
    consumers: NotRequired["capo_kinesis.types.consumer_list.ConsumerList"]
    """<p>An array of JSON objects. Each object represents one registered consumer.</p>"""
    next_token: NotRequired["capo_kinesis.types.next_token.NextToken"]
    """<p>When the number of consumers that are registered with the data stream is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of registered consumers, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListStreamConsumers</code> to list the next set of registered consumers. For more information about the use of this pagination token when calling the <code>ListStreamConsumers</code> operation, see <a>ListStreamConsumersInput$NextToken</a>.</p> <important> <p>Tokens expire after 300 seconds. When you obtain a value for <code>NextToken</code> in the response to a call to <code>ListStreamConsumers</code>, you have 300 seconds to use that value. If you specify an expired token in a call to <code>ListStreamConsumers</code>, you get <code>ExpiredNextTokenException</code>.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStreamConsumersOutput) -> dict:
    out: dict = {}
    if "consumers" in value:
        import capo_kinesis.types.consumer_list

        out["Consumers"] = capo_kinesis.types.consumer_list.serialize_aws_json_1_1(
            value["consumers"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStreamConsumersOutput:
    out: ListStreamConsumersOutput = {}  # type: ignore[typeddict-item]
    if "Consumers" in data:
        import capo_kinesis.types.consumer_list

        out["consumers"] = capo_kinesis.types.consumer_list.deserialize_aws_json_1_1(
            data["Consumers"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
