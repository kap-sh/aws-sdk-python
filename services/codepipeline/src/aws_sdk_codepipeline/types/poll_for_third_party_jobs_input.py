"""Generated from Smithy shape ``com.amazonaws.codepipeline#PollForThirdPartyJobsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_type_id
    import aws_sdk_codepipeline.types.max_batch_size


class PollForThirdPartyJobsInput(TypedDict):
    action_type_id: "aws_sdk_codepipeline.types.action_type_id.ActionTypeId"
    """<p>Represents information about an action type.</p>"""
    max_batch_size: NotRequired[
        "aws_sdk_codepipeline.types.max_batch_size.MaxBatchSize"
    ]
    """<p>The maximum number of jobs to return in a poll for jobs call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PollForThirdPartyJobsInput) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.action_type_id

    out["actionTypeId"] = (
        aws_sdk_codepipeline.types.action_type_id.serialize_aws_json_1_1(
            value["action_type_id"]
        )
    )
    if "max_batch_size" in value:
        out["maxBatchSize"] = value["max_batch_size"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PollForThirdPartyJobsInput:
    out: PollForThirdPartyJobsInput = {}  # type: ignore[typeddict-item]
    if "actionTypeId" in data:
        import aws_sdk_codepipeline.types.action_type_id

        out["action_type_id"] = (
            aws_sdk_codepipeline.types.action_type_id.deserialize_aws_json_1_1(
                data["actionTypeId"]
            )
        )
    else:
        raise DeserializationError("PollForThirdPartyJobsInput.action_type_id required")
    if "maxBatchSize" in data:
        out["max_batch_size"] = data["maxBatchSize"]
    return out
