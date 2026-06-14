"""Generated from Smithy shape ``com.amazonaws.rekognition#ConnectedHomeSettingsForUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.connected_home_labels
    import aws_sdk_rekognition.types.percent


class ConnectedHomeSettingsForUpdate(TypedDict):
    labels: NotRequired[
        "aws_sdk_rekognition.types.connected_home_labels.ConnectedHomeLabels"
    ]
    r"""<p> Specifies what you want to detect in the video, such as people, packages, or pets. The current valid labels you can include in this list are: \"PERSON\", \"PET\", \"PACKAGE\", and \"ALL\". </p>"""
    min_confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p> The minimum confidence required to label an object in the video. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectedHomeSettingsForUpdate) -> dict:
    out: dict = {}
    if "labels" in value:
        import aws_sdk_rekognition.types.connected_home_labels

        out["Labels"] = (
            aws_sdk_rekognition.types.connected_home_labels.serialize_aws_json_1_1(
                value["labels"]
            )
        )
    if "min_confidence" in value:
        out["MinConfidence"] = value["min_confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectedHomeSettingsForUpdate:
    out: ConnectedHomeSettingsForUpdate = {}  # type: ignore[typeddict-item]
    if "Labels" in data:
        import aws_sdk_rekognition.types.connected_home_labels

        out["labels"] = (
            aws_sdk_rekognition.types.connected_home_labels.deserialize_aws_json_1_1(
                data["Labels"]
            )
        )
    if "MinConfidence" in data:
        out["min_confidence"] = data["MinConfidence"]
    return out
