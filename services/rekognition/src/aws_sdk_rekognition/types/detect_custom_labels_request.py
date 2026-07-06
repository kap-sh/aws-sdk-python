"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectCustomLabelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.image
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.project_version_arn
    import aws_sdk_rekognition.types.u_integer


class DetectCustomLabelsRequest(TypedDict, closed=True):
    project_version_arn: (
        "aws_sdk_rekognition.types.project_version_arn.ProjectVersionArn"
    )
    """<p>The ARN of the model version that you want to use. Only models associated with Custom Labels projects accepted by the operation. If a provided ARN refers to a model version associated with a project for a different feature type, then an InvalidParameterException is returned.</p>"""
    image: "aws_sdk_rekognition.types.image.Image"
    max_results: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p>Maximum number of results you want the service to return in the response. The service returns the specified number of highest confidence labels ranked from highest confidence to lowest.</p>"""
    min_confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Specifies the minimum confidence level for the labels to return. <code>DetectCustomLabels</code> doesn't return any labels with a confidence value that's lower than this specified value. If you specify a value of 0, <code>DetectCustomLabels</code> returns all labels, regardless of the assumed threshold applied to each label. If you don't specify a value for <code>MinConfidence</code>, <code>DetectCustomLabels</code> returns labels based on the assumed threshold of each label.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectCustomLabelsRequest) -> dict:
    out: dict = {}
    out["ProjectVersionArn"] = value["project_version_arn"]
    import aws_sdk_rekognition.types.image

    out["Image"] = aws_sdk_rekognition.types.image.serialize_aws_json_1_1(
        value["image"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "min_confidence" in value:
        out["MinConfidence"] = value["min_confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectCustomLabelsRequest:
    out: DetectCustomLabelsRequest = {}  # type: ignore[typeddict-item]
    if "ProjectVersionArn" in data:
        out["project_version_arn"] = data["ProjectVersionArn"]
    else:
        raise DeserializationError(
            "DetectCustomLabelsRequest.project_version_arn required"
        )
    if "Image" in data:
        import aws_sdk_rekognition.types.image

        out["image"] = aws_sdk_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("DetectCustomLabelsRequest.image required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "MinConfidence" in data:
        out["min_confidence"] = data["MinConfidence"]
    return out
