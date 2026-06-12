"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#TimeBasedSignalFetchConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.positive_long


class TimeBasedSignalFetchConfig(TypedDict):
    execution_frequency_ms: "aws_sdk_iotfleetwise.types.positive_long.positiveLong"
    """<p>The frequency with which the signal fetch will be executed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimeBasedSignalFetchConfig) -> dict:
    out: dict = {}
    out["executionFrequencyMs"] = value["execution_frequency_ms"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimeBasedSignalFetchConfig:
    out: TimeBasedSignalFetchConfig = {}  # type: ignore[typeddict-item]
    if "executionFrequencyMs" in data:
        out["execution_frequency_ms"] = data["executionFrequencyMs"]
    else:
        raise DeserializationError(
            "TimeBasedSignalFetchConfig.execution_frequency_ms required"
        )
    return out
