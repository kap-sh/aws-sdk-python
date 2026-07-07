"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectModerationLabelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.content_types
    import aws_sdk_rekognition.types.human_loop_activation_output
    import aws_sdk_rekognition.types.moderation_labels
    import aws_sdk_rekognition.types.project_version_id
    import aws_sdk_rekognition.types.string


class DetectModerationLabelsResponse(TypedDict, closed=True):
    moderation_labels: NotRequired[
        "aws_sdk_rekognition.types.moderation_labels.ModerationLabels"
    ]
    """<p>Array of detected Moderation labels. For video operations, this includes the time, in milliseconds from the start of the video, they were detected.</p>"""
    moderation_model_version: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>Version number of the base moderation detection model that was used to detect unsafe content.</p>"""
    human_loop_activation_output: NotRequired[
        "aws_sdk_rekognition.types.human_loop_activation_output.HumanLoopActivationOutput"
    ]
    """<p>Shows the results of the human in the loop evaluation.</p>"""
    project_version: NotRequired[
        "aws_sdk_rekognition.types.project_version_id.ProjectVersionId"
    ]
    """<p>Identifier of the custom adapter that was used during inference. If during inference the adapter was EXPIRED, then the parameter will not be returned, indicating that a base moderation detection project version was used.</p>"""
    content_types: NotRequired["aws_sdk_rekognition.types.content_types.ContentTypes"]
    """<p>A list of predicted results for the type of content an image contains. For example, the image content might be from animation, sports, or a video game.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectModerationLabelsResponse) -> dict:
    out: dict = {}
    if "moderation_labels" in value:
        import aws_sdk_rekognition.types.moderation_labels

        out["ModerationLabels"] = (
            aws_sdk_rekognition.types.moderation_labels.serialize_aws_json_1_1(
                value["moderation_labels"]
            )
        )
    if "moderation_model_version" in value:
        out["ModerationModelVersion"] = value["moderation_model_version"]
    if "human_loop_activation_output" in value:
        import aws_sdk_rekognition.types.human_loop_activation_output

        out["HumanLoopActivationOutput"] = (
            aws_sdk_rekognition.types.human_loop_activation_output.serialize_aws_json_1_1(
                value["human_loop_activation_output"]
            )
        )
    if "project_version" in value:
        out["ProjectVersion"] = value["project_version"]
    if "content_types" in value:
        import aws_sdk_rekognition.types.content_types

        out["ContentTypes"] = (
            aws_sdk_rekognition.types.content_types.serialize_aws_json_1_1(
                value["content_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectModerationLabelsResponse:
    out: DetectModerationLabelsResponse = {}  # type: ignore[typeddict-item]
    if "ModerationLabels" in data:
        import aws_sdk_rekognition.types.moderation_labels

        out["moderation_labels"] = (
            aws_sdk_rekognition.types.moderation_labels.deserialize_aws_json_1_1(
                data["ModerationLabels"]
            )
        )
    if "ModerationModelVersion" in data:
        out["moderation_model_version"] = data["ModerationModelVersion"]
    if "HumanLoopActivationOutput" in data:
        import aws_sdk_rekognition.types.human_loop_activation_output

        out["human_loop_activation_output"] = (
            aws_sdk_rekognition.types.human_loop_activation_output.deserialize_aws_json_1_1(
                data["HumanLoopActivationOutput"]
            )
        )
    if "ProjectVersion" in data:
        out["project_version"] = data["ProjectVersion"]
    if "ContentTypes" in data:
        import aws_sdk_rekognition.types.content_types

        out["content_types"] = (
            aws_sdk_rekognition.types.content_types.deserialize_aws_json_1_1(
                data["ContentTypes"]
            )
        )
    return out
