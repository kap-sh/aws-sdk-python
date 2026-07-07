"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateTimeToLiveOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.time_to_live_specification


class UpdateTimeToLiveOutput(TypedDict, closed=True):
    time_to_live_specification: NotRequired[
        "aws_sdk_dynamodb.types.time_to_live_specification.TimeToLiveSpecification"
    ]
    """<p>Represents the output of an <code>UpdateTimeToLive</code> operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTimeToLiveOutput) -> dict:
    out: dict = {}
    if "time_to_live_specification" in value:
        import aws_sdk_dynamodb.types.time_to_live_specification

        out["TimeToLiveSpecification"] = (
            aws_sdk_dynamodb.types.time_to_live_specification.serialize_aws_json_1_0(
                value["time_to_live_specification"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTimeToLiveOutput:
    out: UpdateTimeToLiveOutput = {}  # type: ignore[typeddict-item]
    if "TimeToLiveSpecification" in data:
        import aws_sdk_dynamodb.types.time_to_live_specification

        out["time_to_live_specification"] = (
            aws_sdk_dynamodb.types.time_to_live_specification.deserialize_aws_json_1_0(
                data["TimeToLiveSpecification"]
            )
        )
    return out
