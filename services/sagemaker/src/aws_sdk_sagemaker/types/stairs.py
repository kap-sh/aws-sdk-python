"""Generated from Smithy shape ``com.amazonaws.sagemaker#Stairs``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.number_of_steps
    import aws_sdk_sagemaker.types.traffic_duration_in_seconds
    import aws_sdk_sagemaker.types.users_per_step


class Stairs(TypedDict):
    duration_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.traffic_duration_in_seconds.TrafficDurationInSeconds"
    ]
    """<p>Defines how long each traffic step should be.</p>"""
    number_of_steps: NotRequired[
        "aws_sdk_sagemaker.types.number_of_steps.NumberOfSteps"
    ]
    """<p>Specifies how many steps to perform during traffic.</p>"""
    users_per_step: NotRequired["aws_sdk_sagemaker.types.users_per_step.UsersPerStep"]
    """<p>Specifies how many new users to spawn in each step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Stairs) -> dict:
    out: dict = {}
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    if "number_of_steps" in value:
        out["NumberOfSteps"] = value["number_of_steps"]
    if "users_per_step" in value:
        out["UsersPerStep"] = value["users_per_step"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Stairs:
    out: Stairs = {}  # type: ignore[typeddict-item]
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    if "NumberOfSteps" in data:
        out["number_of_steps"] = data["NumberOfSteps"]
    if "UsersPerStep" in data:
        out["users_per_step"] = data["UsersPerStep"]
    return out
