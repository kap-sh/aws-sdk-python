"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.detect_labels_feature_list
    import aws_sdk_rekognition.types.detect_labels_settings
    import aws_sdk_rekognition.types.image
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.u_integer


class DetectLabelsRequest(TypedDict):
    image: "aws_sdk_rekognition.types.image.Image"
    """<p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. Images stored in an S3 Bucket do not need to be base64-encoded.</p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>"""
    max_labels: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p>Maximum number of labels you want the service to return in the response. The service returns the specified number of highest confidence labels. Only valid when GENERAL_LABELS is specified as a feature type in the Feature input parameter.</p>"""
    min_confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with confidence lower than this specified value.</p> <p>If <code>MinConfidence</code> is not specified, the operation returns labels with a confidence values greater than or equal to 55 percent. Only valid when GENERAL_LABELS is specified as a feature type in the Feature input parameter.</p>"""
    features: NotRequired[
        "aws_sdk_rekognition.types.detect_labels_feature_list.DetectLabelsFeatureList"
    ]
    """<p>A list of the types of analysis to perform. Specifying GENERAL_LABELS uses the label detection feature, while specifying IMAGE_PROPERTIES returns information regarding image color and quality. If no option is specified GENERAL_LABELS is used by default.</p>"""
    settings: NotRequired[
        "aws_sdk_rekognition.types.detect_labels_settings.DetectLabelsSettings"
    ]
    r"""<p>A list of the filters to be applied to returned detected labels and image properties. Specified filters can be inclusive, exclusive, or a combination of both. Filters can be used for individual labels or label categories. The exact label names or label categories must be supplied. For a full list of labels and label categories, see <a href=\"https://docs.aws.amazon.com/rekognition/latest/dg/labels.html\">Detecting labels</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectLabelsRequest) -> dict:
    out: dict = {}
    import aws_sdk_rekognition.types.image

    out["Image"] = aws_sdk_rekognition.types.image.serialize_aws_json_1_1(
        value["image"]
    )
    if "max_labels" in value:
        out["MaxLabels"] = value["max_labels"]
    if "min_confidence" in value:
        out["MinConfidence"] = value["min_confidence"]
    if "features" in value:
        import aws_sdk_rekognition.types.detect_labels_feature_list

        out["Features"] = (
            aws_sdk_rekognition.types.detect_labels_feature_list.serialize_aws_json_1_1(
                value["features"]
            )
        )
    if "settings" in value:
        import aws_sdk_rekognition.types.detect_labels_settings

        out["Settings"] = (
            aws_sdk_rekognition.types.detect_labels_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectLabelsRequest:
    out: DetectLabelsRequest = {}  # type: ignore[typeddict-item]
    if "Image" in data:
        import aws_sdk_rekognition.types.image

        out["image"] = aws_sdk_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("DetectLabelsRequest.image required")
    if "MaxLabels" in data:
        out["max_labels"] = data["MaxLabels"]
    if "MinConfidence" in data:
        out["min_confidence"] = data["MinConfidence"]
    if "Features" in data:
        import aws_sdk_rekognition.types.detect_labels_feature_list

        out["features"] = (
            aws_sdk_rekognition.types.detect_labels_feature_list.deserialize_aws_json_1_1(
                data["Features"]
            )
        )
    if "Settings" in data:
        import aws_sdk_rekognition.types.detect_labels_settings

        out["settings"] = (
            aws_sdk_rekognition.types.detect_labels_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    return out
