"""Generated from Smithy shape ``com.amazonaws.dynamodb#ProvisionedThroughputDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.date
    import capo_dynamodb.types.non_negative_long_object
    import capo_dynamodb.types.positive_long_object


class ProvisionedThroughputDescription(TypedDict, closed=True):
    last_increase_date_time: NotRequired["capo_dynamodb.types.date.Date"]
    """<p>The date and time of the last provisioned throughput increase for this table.</p>"""
    last_decrease_date_time: NotRequired["capo_dynamodb.types.date.Date"]
    """<p>The date and time of the last provisioned throughput decrease for this table.</p>"""
    number_of_decreases_today: NotRequired[
        "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    ]
    r"""<p>The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html\">Service, Account, and Table Quotas</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    read_capacity_units: NotRequired[
        "capo_dynamodb.types.non_negative_long_object.NonNegativeLongObject"
    ]
    """<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>. Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 <code>ReadCapacityUnits</code> per second provides 100 eventually consistent <code>ReadCapacityUnits</code> per second.</p>"""
    write_capacity_units: NotRequired[
        "capo_dynamodb.types.non_negative_long_object.NonNegativeLongObject"
    ]
    """<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProvisionedThroughputDescription) -> dict:
    out: dict = {}
    if "last_increase_date_time" in value:
        import capo_dynamodb.types.date

        out["LastIncreaseDateTime"] = capo_dynamodb.types.date.serialize_aws_json_1_0(
            value["last_increase_date_time"]
        )
    if "last_decrease_date_time" in value:
        import capo_dynamodb.types.date

        out["LastDecreaseDateTime"] = capo_dynamodb.types.date.serialize_aws_json_1_0(
            value["last_decrease_date_time"]
        )
    if "number_of_decreases_today" in value:
        out["NumberOfDecreasesToday"] = value["number_of_decreases_today"]
    if "read_capacity_units" in value:
        out["ReadCapacityUnits"] = value["read_capacity_units"]
    if "write_capacity_units" in value:
        out["WriteCapacityUnits"] = value["write_capacity_units"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProvisionedThroughputDescription:
    out: ProvisionedThroughputDescription = {}  # type: ignore[typeddict-item]
    if "LastIncreaseDateTime" in data:
        import capo_dynamodb.types.date

        out["last_increase_date_time"] = (
            capo_dynamodb.types.date.deserialize_aws_json_1_0(
                data["LastIncreaseDateTime"]
            )
        )
    if "LastDecreaseDateTime" in data:
        import capo_dynamodb.types.date

        out["last_decrease_date_time"] = (
            capo_dynamodb.types.date.deserialize_aws_json_1_0(
                data["LastDecreaseDateTime"]
            )
        )
    if "NumberOfDecreasesToday" in data:
        out["number_of_decreases_today"] = data["NumberOfDecreasesToday"]
    if "ReadCapacityUnits" in data:
        out["read_capacity_units"] = data["ReadCapacityUnits"]
    if "WriteCapacityUnits" in data:
        out["write_capacity_units"] = data["WriteCapacityUnits"]
    return out
