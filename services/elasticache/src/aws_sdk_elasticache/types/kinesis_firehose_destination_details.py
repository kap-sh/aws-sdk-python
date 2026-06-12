"""Generated from Smithy shape ``com.amazonaws.elasticache#KinesisFirehoseDestinationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class KinesisFirehoseDestinationDetails(TypedDict):
    delivery_stream: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the Kinesis Data Firehose delivery stream.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: KinesisFirehoseDestinationDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "delivery_stream" in value:
        pairs.append((f"{prefix}.DeliveryStream", str(value["delivery_stream"])))


def deserialize_query(el: Element) -> KinesisFirehoseDestinationDetails:
    out: KinesisFirehoseDestinationDetails = {}  # type: ignore[typeddict-item]
    child_delivery_stream = el.find("DeliveryStream")
    if child_delivery_stream is not None:
        out["delivery_stream"] = str(child_delivery_stream.text or "")
    return out
