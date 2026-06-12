"""Generated from Smithy shape ``com.amazonaws.rekognition#CompareFacesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.image
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.quality_filter


class CompareFacesRequest(TypedDict):
    source_image: "aws_sdk_rekognition.types.image.Image"
    """<p>The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>"""
    target_image: "aws_sdk_rekognition.types.image.Image"
    """<p>The target image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. </p> <p>If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. For more information, see Images in the Amazon Rekognition developer guide.</p>"""
    similarity_threshold: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The minimum level of confidence in the face matches that a match must meet to be included in the <code>FaceMatches</code> array.</p>"""
    quality_filter: NotRequired[
        "aws_sdk_rekognition.types.quality_filter.QualityFilter"
    ]
    """<p>A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces aren't compared. If you specify <code>AUTO</code>, Amazon Rekognition chooses the quality bar. If you specify <code>LOW</code>, <code>MEDIUM</code>, or <code>HIGH</code>, filtering removes all faces that don’t meet the chosen quality bar. The quality bar is based on a variety of common use cases. Low-quality detections can occur for a number of reasons. Some examples are an object that's misidentified as a face, a face that's too blurry, or a face with a pose that's too extreme to use. If you specify <code>NONE</code>, no filtering is performed. The default value is <code>NONE</code>. </p> <p>To use quality filtering, the collection you are using must be associated with version 3 of the face model or higher.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompareFacesRequest) -> dict:
    out: dict = {}
    import aws_sdk_rekognition.types.image

    out["SourceImage"] = aws_sdk_rekognition.types.image.serialize_aws_json_1_1(
        value["source_image"]
    )
    import aws_sdk_rekognition.types.image

    out["TargetImage"] = aws_sdk_rekognition.types.image.serialize_aws_json_1_1(
        value["target_image"]
    )
    if "similarity_threshold" in value:
        out["SimilarityThreshold"] = value["similarity_threshold"]
    if "quality_filter" in value:
        import aws_sdk_rekognition.types.quality_filter

        out["QualityFilter"] = (
            aws_sdk_rekognition.types.quality_filter.serialize_aws_json_1_1(
                value["quality_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompareFacesRequest:
    out: CompareFacesRequest = {}  # type: ignore[typeddict-item]
    if "SourceImage" in data:
        import aws_sdk_rekognition.types.image

        out["source_image"] = aws_sdk_rekognition.types.image.deserialize_aws_json_1_1(
            data["SourceImage"]
        )
    else:
        raise DeserializationError("CompareFacesRequest.source_image required")
    if "TargetImage" in data:
        import aws_sdk_rekognition.types.image

        out["target_image"] = aws_sdk_rekognition.types.image.deserialize_aws_json_1_1(
            data["TargetImage"]
        )
    else:
        raise DeserializationError("CompareFacesRequest.target_image required")
    if "SimilarityThreshold" in data:
        out["similarity_threshold"] = data["SimilarityThreshold"]
    if "QualityFilter" in data:
        import aws_sdk_rekognition.types.quality_filter

        out["quality_filter"] = (
            aws_sdk_rekognition.types.quality_filter.deserialize_aws_json_1_1(
                data["QualityFilter"]
            )
        )
    return out
