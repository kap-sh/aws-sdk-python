"""Generated from Smithy shape ``com.amazonaws.sfn#DeleteActivityInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn


class DeleteActivityInput(TypedDict):
    activity_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the activity to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteActivityInput) -> dict:
    out: dict = {}
    out["activityArn"] = value["activity_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteActivityInput:
    out: DeleteActivityInput = {}  # type: ignore[typeddict-item]
    if "activityArn" in data:
        out["activity_arn"] = data["activityArn"]
    else:
        raise DeserializationError("DeleteActivityInput.activity_arn required")
    return out
