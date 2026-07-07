"""Generated from Smithy shape ``com.amazonaws.sfn#CreateActivityOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.timestamp


class CreateActivityOutput(TypedDict, closed=True):
    activity_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the created activity.</p>"""
    creation_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date the activity is created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateActivityOutput) -> dict:
    out: dict = {}
    out["activityArn"] = value["activity_arn"]
    import aws_sdk_sfn.types.timestamp

    out["creationDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateActivityOutput:
    out: CreateActivityOutput = {}  # type: ignore[typeddict-item]
    if "activityArn" in data:
        out["activity_arn"] = data["activityArn"]
    else:
        raise DeserializationError("CreateActivityOutput.activity_arn required")
    if "creationDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["creation_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        raise DeserializationError("CreateActivityOutput.creation_date required")
    return out
