"""Generated from Smithy shape ``com.amazonaws.dynamodb#StreamSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.stream_enabled
    import aws_sdk_dynamodb.types.stream_view_type


class StreamSpecification(TypedDict):
    stream_enabled: "aws_sdk_dynamodb.types.stream_enabled.StreamEnabled"
    """<p>Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.</p>"""
    stream_view_type: NotRequired[
        "aws_sdk_dynamodb.types.stream_view_type.StreamViewType"
    ]
    """<p> When an item in the table is modified, <code>StreamViewType</code> determines what information is written to the stream for this table. Valid values for <code>StreamViewType</code> are:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - Only the key attributes of the modified item are written to the stream.</p> </li> <li> <p> <code>NEW_IMAGE</code> - The entire item, as it appears after it was modified, is written to the stream.</p> </li> <li> <p> <code>OLD_IMAGE</code> - The entire item, as it appeared before it was modified, is written to the stream.</p> </li> <li> <p> <code>NEW_AND_OLD_IMAGES</code> - Both the new and the old item images of the item are written to the stream.</p> </li> </ul>"""
