"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectModerationLabelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.human_loop_config
    import aws_sdk_rekognition.types.image
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.project_version_id


class DetectModerationLabelsRequest(TypedDict):
    image: "aws_sdk_rekognition.types.image.Image"
    """<p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>"""
    min_confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with a confidence level lower than this specified value.</p> <p>If you don't specify <code>MinConfidence</code>, the operation returns labels with confidence values greater than or equal to 50 percent.</p>"""
    human_loop_config: NotRequired[
        "aws_sdk_rekognition.types.human_loop_config.HumanLoopConfig"
    ]
    """<p>Sets up the configuration for human evaluation, including the FlowDefinition the image will be sent to.</p>"""
    project_version: NotRequired[
        "aws_sdk_rekognition.types.project_version_id.ProjectVersionId"
    ]
    """<p>Identifier for the custom adapter. Expects the ProjectVersionArn as a value. Use the CreateProject or CreateProjectVersion APIs to create a custom adapter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectModerationLabelsRequest) -> dict:
    out: dict = {}
    import aws_sdk_rekognition.types.image

    out["Image"] = aws_sdk_rekognition.types.image.serialize_aws_json_1_1(
        value["image"]
    )
    if "min_confidence" in value:
        out["MinConfidence"] = value["min_confidence"]
    if "human_loop_config" in value:
        import aws_sdk_rekognition.types.human_loop_config

        out["HumanLoopConfig"] = (
            aws_sdk_rekognition.types.human_loop_config.serialize_aws_json_1_1(
                value["human_loop_config"]
            )
        )
    if "project_version" in value:
        out["ProjectVersion"] = value["project_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectModerationLabelsRequest:
    out: DetectModerationLabelsRequest = {}  # type: ignore[typeddict-item]
    if "Image" in data:
        import aws_sdk_rekognition.types.image

        out["image"] = aws_sdk_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("DetectModerationLabelsRequest.image required")
    if "MinConfidence" in data:
        out["min_confidence"] = data["MinConfidence"]
    if "HumanLoopConfig" in data:
        import aws_sdk_rekognition.types.human_loop_config

        out["human_loop_config"] = (
            aws_sdk_rekognition.types.human_loop_config.deserialize_aws_json_1_1(
                data["HumanLoopConfig"]
            )
        )
    if "ProjectVersion" in data:
        out["project_version"] = data["ProjectVersion"]
    return out
