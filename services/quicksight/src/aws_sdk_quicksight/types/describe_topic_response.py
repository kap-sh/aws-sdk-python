"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTopicResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.custom_instructions
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.topic_details
    import aws_sdk_quicksight.types.topic_id


class DescribeTopicResponse(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    topic_id: NotRequired["aws_sdk_quicksight.types.topic_id.TopicId"]
    """<p>The ID of the topic that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    topic: NotRequired["aws_sdk_quicksight.types.topic_details.TopicDetails"]
    """<p>The definition of a topic.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    custom_instructions: NotRequired[
        "aws_sdk_quicksight.types.custom_instructions.CustomInstructions"
    ]
    """<p>Custom instructions for the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTopicResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "topic" in value:
        import aws_sdk_quicksight.types.topic_details

        out["Topic"] = aws_sdk_quicksight.types.topic_details.serialize_json(
            value["topic"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "custom_instructions" in value:
        import aws_sdk_quicksight.types.custom_instructions

        out["CustomInstructions"] = (
            aws_sdk_quicksight.types.custom_instructions.serialize_json(
                value["custom_instructions"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeTopicResponse:
    out: DescribeTopicResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "TopicId" in data:
        out["topic_id"] = data["TopicId"]
    if "Topic" in data:
        import aws_sdk_quicksight.types.topic_details

        out["topic"] = aws_sdk_quicksight.types.topic_details.deserialize_json(
            data["Topic"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "CustomInstructions" in data:
        import aws_sdk_quicksight.types.custom_instructions

        out["custom_instructions"] = (
            aws_sdk_quicksight.types.custom_instructions.deserialize_json(
                data["CustomInstructions"]
            )
        )
    return out
