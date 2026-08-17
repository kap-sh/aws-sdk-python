"""Generated from Smithy shape ``com.amazonaws.dynamodb#OnDemandThroughput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.long_object


class OnDemandThroughput(TypedDict, closed=True):
    max_read_request_units: NotRequired["capo_dynamodb.types.long_object.LongObject"]
    """<p>Maximum number of read request units for the specified table.</p> <p>To specify a maximum <code>OnDemandThroughput</code> on your table, set the value of <code>MaxReadRequestUnits</code> as greater than or equal to 1. To remove the maximum <code>OnDemandThroughput</code> that is currently set on your table, set the value of <code>MaxReadRequestUnits</code> to -1.</p>"""
    max_write_request_units: NotRequired["capo_dynamodb.types.long_object.LongObject"]
    """<p>Maximum number of write request units for the specified table.</p> <p>To specify a maximum <code>OnDemandThroughput</code> on your table, set the value of <code>MaxWriteRequestUnits</code> as greater than or equal to 1. To remove the maximum <code>OnDemandThroughput</code> that is currently set on your table, set the value of <code>MaxWriteRequestUnits</code> to -1.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OnDemandThroughput) -> dict:
    out: dict = {}
    if "max_read_request_units" in value:
        out["MaxReadRequestUnits"] = value["max_read_request_units"]
    if "max_write_request_units" in value:
        out["MaxWriteRequestUnits"] = value["max_write_request_units"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OnDemandThroughput:
    out: OnDemandThroughput = {}  # type: ignore[typeddict-item]
    if data.get("MaxReadRequestUnits") is not None:
        out["max_read_request_units"] = data["MaxReadRequestUnits"]
    if data.get("MaxWriteRequestUnits") is not None:
        out["max_write_request_units"] = data["MaxWriteRequestUnits"]
    return out
