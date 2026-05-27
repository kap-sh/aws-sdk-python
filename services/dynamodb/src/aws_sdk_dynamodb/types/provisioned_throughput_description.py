"""Generated from Smithy shape ``com.amazonaws.dynamodb#ProvisionedThroughputDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.date
    import aws_sdk_dynamodb.types.non_negative_long_object
    import aws_sdk_dynamodb.types.positive_long_object


class ProvisionedThroughputDescription(TypedDict):
    last_increase_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p>The date and time of the last provisioned throughput increase for this table.</p>"""
    last_decrease_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p>The date and time of the last provisioned throughput decrease for this table.</p>"""
    number_of_decreases_today: NotRequired[
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    """<p>The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html\">Service, Account, and Table Quotas</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    read_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.non_negative_long_object.NonNegativeLongObject"
    ]
    """<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>. Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 <code>ReadCapacityUnits</code> per second provides 100 eventually consistent <code>ReadCapacityUnits</code> per second.</p>"""
    write_capacity_units: NotRequired[
        "aws_sdk_dynamodb.types.non_negative_long_object.NonNegativeLongObject"
    ]
    """<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException</code>.</p>"""
