"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectTextRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.detect_text_filters
    import capo_rekognition.types.image


class DetectTextRequest(TypedDict, closed=True):
    image: "capo_rekognition.types.image.Image"
    """<p>The input image as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Rekognition operations, you can't pass image bytes. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>"""
    filters: NotRequired["capo_rekognition.types.detect_text_filters.DetectTextFilters"]
    """<p>Optional parameters that let you set the criteria that the text must meet to be included in your response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectTextRequest) -> dict:
    out: dict = {}
    import capo_rekognition.types.image

    out["Image"] = capo_rekognition.types.image.serialize_aws_json_1_1(value["image"])
    if "filters" in value:
        import capo_rekognition.types.detect_text_filters

        out["Filters"] = (
            capo_rekognition.types.detect_text_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectTextRequest:
    out: DetectTextRequest = {}  # type: ignore[typeddict-item]
    if "Image" in data:
        import capo_rekognition.types.image

        out["image"] = capo_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("DetectTextRequest.image required")
    if "Filters" in data:
        import capo_rekognition.types.detect_text_filters

        out["filters"] = (
            capo_rekognition.types.detect_text_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
