"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableProvisionedThroughput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsDynamoDbTableProvisionedThroughput(TypedDict):
    last_decrease_date_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the provisioned throughput was last decreased.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    last_increase_date_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the provisioned throughput was last increased.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    number_of_decreases_today: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of times during the current UTC calendar day that the provisioned throughput was decreased.</p>"""
    read_capacity_units: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>.</p>"""
    write_capacity_units: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableProvisionedThroughput) -> dict:
    out: dict = {}
    if "last_decrease_date_time" in value:
        out["LastDecreaseDateTime"] = value["last_decrease_date_time"]
    if "last_increase_date_time" in value:
        out["LastIncreaseDateTime"] = value["last_increase_date_time"]
    if "number_of_decreases_today" in value:
        out["NumberOfDecreasesToday"] = value["number_of_decreases_today"]
    if "read_capacity_units" in value:
        out["ReadCapacityUnits"] = value["read_capacity_units"]
    if "write_capacity_units" in value:
        out["WriteCapacityUnits"] = value["write_capacity_units"]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableProvisionedThroughput:
    out: AwsDynamoDbTableProvisionedThroughput = {}  # type: ignore[typeddict-item]
    if "LastDecreaseDateTime" in data:
        out["last_decrease_date_time"] = data["LastDecreaseDateTime"]
    if "LastIncreaseDateTime" in data:
        out["last_increase_date_time"] = data["LastIncreaseDateTime"]
    if "NumberOfDecreasesToday" in data:
        out["number_of_decreases_today"] = data["NumberOfDecreasesToday"]
    if "ReadCapacityUnits" in data:
        out["read_capacity_units"] = data["ReadCapacityUnits"]
    if "WriteCapacityUnits" in data:
        out["write_capacity_units"] = data["WriteCapacityUnits"]
    return out
