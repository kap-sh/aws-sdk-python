"""Generated from Smithy shape ``com.amazonaws.cloudfront#Invalidation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.invalidation_batch
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.timestamp


class Invalidation(TypedDict, closed=True):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier for the invalidation request. For example: <code>IDFDVBD632BHDS5</code>.</p>"""
    status: "aws_sdk_cloudfront.types.string.string"
    """<p>The status of the invalidation request. When the invalidation batch is finished, the status is <code>Completed</code>.</p>"""
    create_time: "aws_sdk_cloudfront.types.timestamp.timestamp"
    """<p>The date and time the invalidation request was first made.</p>"""
    invalidation_batch: "aws_sdk_cloudfront.types.invalidation_batch.InvalidationBatch"
    """<p>The current invalidation information for the batch request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Invalidation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Status").text = str(value["status"])
    import aws_sdk_cloudfront.types.timestamp

    aws_sdk_cloudfront.types.timestamp.serialize_xml(
        value["create_time"], el, "CreateTime"
    )
    import aws_sdk_cloudfront.types.invalidation_batch

    aws_sdk_cloudfront.types.invalidation_batch.serialize_xml(
        value["invalidation_batch"], el, "InvalidationBatch"
    )


def deserialize_xml(el: Element) -> Invalidation:
    out: Invalidation = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("Invalidation.id required")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        raise DeserializationError("Invalidation.status required")
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import aws_sdk_cloudfront.types.timestamp

        out["create_time"] = aws_sdk_cloudfront.types.timestamp.deserialize_xml(
            child_create_time
        )
    else:
        raise DeserializationError("Invalidation.create_time required")
    child_invalidation_batch = el.find("InvalidationBatch")
    if child_invalidation_batch is not None:
        import aws_sdk_cloudfront.types.invalidation_batch

        out["invalidation_batch"] = (
            aws_sdk_cloudfront.types.invalidation_batch.deserialize_xml(
                child_invalidation_batch
            )
        )
    else:
        raise DeserializationError("Invalidation.invalidation_batch required")
    return out
