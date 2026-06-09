"""Generated from Smithy shape ``com.amazonaws.dynamodb#OnDemandThroughputOverride``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.long_object


class OnDemandThroughputOverride(TypedDict):
    max_read_request_units: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>Maximum number of read request units for the specified replica table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OnDemandThroughputOverride) -> dict:
    out: dict = {}
    if "max_read_request_units" in value:
        out["MaxReadRequestUnits"] = value["max_read_request_units"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OnDemandThroughputOverride:
    out: OnDemandThroughputOverride = {}  # type: ignore[typeddict-item]
    if "MaxReadRequestUnits" in data:
        out["max_read_request_units"] = data["MaxReadRequestUnits"]
    return out
