"""Generated from Smithy shape ``com.amazonaws.s3#RecordsEvent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.body


class RecordsEvent(TypedDict):
    payload: NotRequired["aws_sdk_s3.types.body.Body"]
    """<p>The byte array of partial, one or more result records. S3 Select doesn't guarantee that a record will be self-contained in one record frame. To ensure continuous streaming of data, S3 Select might split the same record across multiple record frames instead of aggregating the results in memory. Some S3 clients (for example, the SDK for Java) handle this behavior by creating a <code>ByteStream</code> out of the response by default. Other clients might not handle this behavior by default. In those cases, you must aggregate the results on the client side and parse the response.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: RecordsEvent, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "payload" in value:
        import aws_sdk_s3.types.body

        aws_sdk_s3.types.body.serialize_xml(value["payload"], el, "Payload")


def deserialize_xml(el: Element) -> RecordsEvent:
    out: RecordsEvent = {}  # type: ignore[typeddict-item]
    child_payload = el.find("Payload")
    if child_payload is not None:
        import aws_sdk_s3.types.body

        out["payload"] = aws_sdk_s3.types.body.deserialize_xml(child_payload)
    return out
