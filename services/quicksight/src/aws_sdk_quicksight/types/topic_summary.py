"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_name
    import aws_sdk_quicksight.types.topic_id
    import aws_sdk_quicksight.types.topic_user_experience_version


class TopicSummary(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    topic_id: NotRequired["aws_sdk_quicksight.types.topic_id.TopicId"]
    """<p>The ID for the topic. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.resource_name.ResourceName"]
    """<p>The name of the topic.</p>"""
    user_experience_version: NotRequired[
        "aws_sdk_quicksight.types.topic_user_experience_version.TopicUserExperienceVersion"
    ]
    """<p>The user experience version of the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "user_experience_version" in value:
        import aws_sdk_quicksight.types.topic_user_experience_version

        out["UserExperienceVersion"] = (
            aws_sdk_quicksight.types.topic_user_experience_version.serialize_json(
                value["user_experience_version"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicSummary:
    out: TopicSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "TopicId" in data:
        out["topic_id"] = data["TopicId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "UserExperienceVersion" in data:
        import aws_sdk_quicksight.types.topic_user_experience_version

        out["user_experience_version"] = (
            aws_sdk_quicksight.types.topic_user_experience_version.deserialize_json(
                data["UserExperienceVersion"]
            )
        )
    return out
