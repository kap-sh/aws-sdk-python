"""Generated from Smithy shape ``com.amazonaws.lambda#SelfManagedEventSource``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.endpoints


class SelfManagedEventSource(TypedDict):
    endpoints: NotRequired["aws_sdk_lambda.types.endpoints.Endpoints"]
    """<p>The list of bootstrap servers for your Kafka brokers in the following format: <code>\"KAFKA_BOOTSTRAP_SERVERS\": [\"abc.xyz.com:xxxx\",\"abc2.xyz.com:xxxx\"]</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedEventSource) -> dict:
    out: dict = {}
    if "endpoints" in value:
        import aws_sdk_lambda.types.endpoints

        out["Endpoints"] = aws_sdk_lambda.types.endpoints.serialize_json(
            value["endpoints"]
        )
    return out


def deserialize_json(data: dict) -> SelfManagedEventSource:
    out: SelfManagedEventSource = {}  # type: ignore[typeddict-item]
    if "Endpoints" in data:
        import aws_sdk_lambda.types.endpoints

        out["endpoints"] = aws_sdk_lambda.types.endpoints.deserialize_json(
            data["Endpoints"]
        )
    return out
