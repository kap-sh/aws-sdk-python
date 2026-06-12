"""Generated from Smithy shape ``com.amazonaws.sagemaker#Phase``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.initial_number_of_users
    import aws_sdk_sagemaker.types.spawn_rate
    import aws_sdk_sagemaker.types.traffic_duration_in_seconds


class Phase(TypedDict):
    initial_number_of_users: NotRequired[
        "aws_sdk_sagemaker.types.initial_number_of_users.InitialNumberOfUsers"
    ]
    """<p>Specifies how many concurrent users to start with. The value should be between 1 and 3.</p>"""
    spawn_rate: NotRequired["aws_sdk_sagemaker.types.spawn_rate.SpawnRate"]
    """<p>Specified how many new users to spawn in a minute.</p>"""
    duration_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.traffic_duration_in_seconds.TrafficDurationInSeconds"
    ]
    """<p>Specifies how long a traffic phase should be. For custom load tests, the value should be between 120 and 3600. This value should not exceed <code>JobDurationInSeconds</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Phase) -> dict:
    out: dict = {}
    if "initial_number_of_users" in value:
        out["InitialNumberOfUsers"] = value["initial_number_of_users"]
    if "spawn_rate" in value:
        out["SpawnRate"] = value["spawn_rate"]
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Phase:
    out: Phase = {}  # type: ignore[typeddict-item]
    if "InitialNumberOfUsers" in data:
        out["initial_number_of_users"] = data["InitialNumberOfUsers"]
    if "SpawnRate" in data:
        out["spawn_rate"] = data["SpawnRate"]
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    return out
