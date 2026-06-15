"""Generated from Smithy shape ``com.amazonaws.keyspaces#CapacitySpecificationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.capacity_units
    import aws_sdk_keyspaces.types.throughput_mode
    import aws_sdk_keyspaces.types.timestamp


class CapacitySpecificationSummary(TypedDict):
    throughput_mode: "aws_sdk_keyspaces.types.throughput_mode.ThroughputMode"
    r"""<p>The read/write throughput capacity mode for a table. The options are:</p> <ul> <li> <p> <code>throughputMode:PAY_PER_REQUEST</code> and </p> </li> <li> <p> <code>throughputMode:PROVISIONED</code> - Provisioned capacity mode requires <code>readCapacityUnits</code> and <code>writeCapacityUnits</code> as input. </p> </li> </ul> <p>The default is <code>throughput_mode:PAY_PER_REQUEST</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html\">Read/write capacity modes</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    read_capacity_units: NotRequired[
        "aws_sdk_keyspaces.types.capacity_units.CapacityUnits"
    ]
    """<p>The throughput capacity specified for <code>read</code> operations defined in <code>read capacity units</code> <code>(RCUs)</code>.</p>"""
    write_capacity_units: NotRequired[
        "aws_sdk_keyspaces.types.capacity_units.CapacityUnits"
    ]
    """<p>The throughput capacity specified for <code>write</code> operations defined in <code>write capacity units</code> <code>(WCUs)</code>.</p>"""
    last_update_to_pay_per_request_timestamp: NotRequired[
        "aws_sdk_keyspaces.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the last operation that changed the provisioned throughput capacity of a table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapacitySpecificationSummary) -> dict:
    out: dict = {}
    out["throughputMode"] = value["throughput_mode"]
    if "read_capacity_units" in value:
        out["readCapacityUnits"] = value["read_capacity_units"]
    if "write_capacity_units" in value:
        out["writeCapacityUnits"] = value["write_capacity_units"]
    if "last_update_to_pay_per_request_timestamp" in value:
        import aws_sdk_keyspaces.types.timestamp

        out["lastUpdateToPayPerRequestTimestamp"] = (
            aws_sdk_keyspaces.types.timestamp.serialize_aws_json_1_0(
                value["last_update_to_pay_per_request_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CapacitySpecificationSummary:
    out: CapacitySpecificationSummary = {}  # type: ignore[typeddict-item]
    if "throughputMode" in data:
        out["throughput_mode"] = data["throughputMode"]
    else:
        raise DeserializationError(
            "CapacitySpecificationSummary.throughput_mode required"
        )
    if "readCapacityUnits" in data:
        out["read_capacity_units"] = data["readCapacityUnits"]
    if "writeCapacityUnits" in data:
        out["write_capacity_units"] = data["writeCapacityUnits"]
    if "lastUpdateToPayPerRequestTimestamp" in data:
        import aws_sdk_keyspaces.types.timestamp

        out["last_update_to_pay_per_request_timestamp"] = (
            aws_sdk_keyspaces.types.timestamp.deserialize_aws_json_1_0(
                data["lastUpdateToPayPerRequestTimestamp"]
            )
        )
    return out
