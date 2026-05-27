"""Generated from Smithy shape ``com.amazonaws.dynamodb#OnDemandThroughput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.long_object


class OnDemandThroughput(TypedDict):
    max_read_request_units: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>Maximum number of read request units for the specified table.</p> <p>To specify a maximum <code>OnDemandThroughput</code> on your table, set the value of <code>MaxReadRequestUnits</code> as greater than or equal to 1. To remove the maximum <code>OnDemandThroughput</code> that is currently set on your table, set the value of <code>MaxReadRequestUnits</code> to -1.</p>"""
    max_write_request_units: NotRequired[
        "aws_sdk_dynamodb.types.long_object.LongObject"
    ]
    """<p>Maximum number of write request units for the specified table.</p> <p>To specify a maximum <code>OnDemandThroughput</code> on your table, set the value of <code>MaxWriteRequestUnits</code> as greater than or equal to 1. To remove the maximum <code>OnDemandThroughput</code> that is currently set on your table, set the value of <code>MaxWriteRequestUnits</code> to -1.</p>"""
