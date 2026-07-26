"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.detect_labels_image_properties
    import capo_rekognition.types.labels
    import capo_rekognition.types.orientation_correction
    import capo_rekognition.types.string


class DetectLabelsResponse(TypedDict, closed=True):
    labels: NotRequired["capo_rekognition.types.labels.Labels"]
    """<p>An array of labels for the real-world objects detected. </p>"""
    orientation_correction: NotRequired[
        "capo_rekognition.types.orientation_correction.OrientationCorrection"
    ]
    """<p>The value of <code>OrientationCorrection</code> is always null.</p> <p>If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the image's orientation. Amazon Rekognition uses this orientation information to perform image correction. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format don't contain Exif metadata.</p> <p>Amazon Rekognition doesn’t perform image correction for images in .png format and .jpeg images without orientation information in the image Exif metadata. The bounding box coordinates aren't translated and represent the object locations before the image is rotated. </p>"""
    label_model_version: NotRequired["capo_rekognition.types.string.String"]
    """<p>Version number of the label detection model that was used to detect labels.</p>"""
    image_properties: NotRequired[
        "capo_rekognition.types.detect_labels_image_properties.DetectLabelsImageProperties"
    ]
    """<p>Information about the properties of the input image, such as brightness, sharpness, contrast, and dominant colors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectLabelsResponse) -> dict:
    out: dict = {}
    if "labels" in value:
        import capo_rekognition.types.labels

        out["Labels"] = capo_rekognition.types.labels.serialize_aws_json_1_1(
            value["labels"]
        )
    if "orientation_correction" in value:
        import capo_rekognition.types.orientation_correction

        out["OrientationCorrection"] = (
            capo_rekognition.types.orientation_correction.serialize_aws_json_1_1(
                value["orientation_correction"]
            )
        )
    if "label_model_version" in value:
        out["LabelModelVersion"] = value["label_model_version"]
    if "image_properties" in value:
        import capo_rekognition.types.detect_labels_image_properties

        out["ImageProperties"] = (
            capo_rekognition.types.detect_labels_image_properties.serialize_aws_json_1_1(
                value["image_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectLabelsResponse:
    out: DetectLabelsResponse = {}  # type: ignore[typeddict-item]
    if "Labels" in data:
        import capo_rekognition.types.labels

        out["labels"] = capo_rekognition.types.labels.deserialize_aws_json_1_1(
            data["Labels"]
        )
    if "OrientationCorrection" in data:
        import capo_rekognition.types.orientation_correction

        out["orientation_correction"] = (
            capo_rekognition.types.orientation_correction.deserialize_aws_json_1_1(
                data["OrientationCorrection"]
            )
        )
    if "LabelModelVersion" in data:
        out["label_model_version"] = data["LabelModelVersion"]
    if "ImageProperties" in data:
        import capo_rekognition.types.detect_labels_image_properties

        out["image_properties"] = (
            capo_rekognition.types.detect_labels_image_properties.deserialize_aws_json_1_1(
                data["ImageProperties"]
            )
        )
    return out
