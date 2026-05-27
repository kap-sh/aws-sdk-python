"""Generated from Smithy shape ``com.amazonaws.dynamodb#ProvisionedThroughput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.positive_long_object


class ProvisionedThroughput(TypedDict):
    read_capacity_units: (
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    )
    """<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html\">Specifying Read and Write Requirements</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>If read/write capacity mode is <code>PAY_PER_REQUEST</code> the value is set to 0.</p>"""
    write_capacity_units: (
        "aws_sdk_dynamodb.types.positive_long_object.PositiveLongObject"
    )
    """<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException</code>. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html\">Specifying Read and Write Requirements</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>If read/write capacity mode is <code>PAY_PER_REQUEST</code> the value is set to 0.</p>"""
