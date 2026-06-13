"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTopicRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.custom_instructions
    import aws_sdk_quicksight.types.topic_details
    import aws_sdk_quicksight.types.topic_id


class UpdateTopicRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the topic that you want to update.</p>"""
    topic_id: "aws_sdk_quicksight.types.topic_id.TopicId"
    """<p>The ID of the topic that you want to modify. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    topic: "aws_sdk_quicksight.types.topic_details.TopicDetails"
    """<p>The definition of the topic that you want to update.</p>"""
    custom_instructions: NotRequired[
        "aws_sdk_quicksight.types.custom_instructions.CustomInstructions"
    ]
    """<p>Custom instructions for the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTopicRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.topic_details

    out["Topic"] = aws_sdk_quicksight.types.topic_details.serialize_json(value["topic"])
    if "custom_instructions" in value:
        import aws_sdk_quicksight.types.custom_instructions

        out["CustomInstructions"] = (
            aws_sdk_quicksight.types.custom_instructions.serialize_json(
                value["custom_instructions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTopicRequest:
    out: UpdateTopicRequest = {}  # type: ignore[typeddict-item]
    if "Topic" in data:
        import aws_sdk_quicksight.types.topic_details

        out["topic"] = aws_sdk_quicksight.types.topic_details.deserialize_json(
            data["Topic"]
        )
    else:
        raise DeserializationError("UpdateTopicRequest.topic required")
    if "CustomInstructions" in data:
        import aws_sdk_quicksight.types.custom_instructions

        out["custom_instructions"] = (
            aws_sdk_quicksight.types.custom_instructions.deserialize_json(
                data["CustomInstructions"]
            )
        )
    return out
