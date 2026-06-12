"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectProtectiveEquipmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.image
    import aws_sdk_rekognition.types.protective_equipment_summarization_attributes


class DetectProtectiveEquipmentRequest(TypedDict):
    image: "aws_sdk_rekognition.types.image.Image"
    """<p>The image in which you want to detect PPE on detected persons. The image can be passed as image bytes or you can reference an image stored in an Amazon S3 bucket. </p>"""
    summarization_attributes: NotRequired[
        "aws_sdk_rekognition.types.protective_equipment_summarization_attributes.ProtectiveEquipmentSummarizationAttributes"
    ]
    """<p>An array of PPE types that you want to summarize.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectProtectiveEquipmentRequest) -> dict:
    out: dict = {}
    import aws_sdk_rekognition.types.image

    out["Image"] = aws_sdk_rekognition.types.image.serialize_aws_json_1_1(
        value["image"]
    )
    if "summarization_attributes" in value:
        import aws_sdk_rekognition.types.protective_equipment_summarization_attributes

        out["SummarizationAttributes"] = (
            aws_sdk_rekognition.types.protective_equipment_summarization_attributes.serialize_aws_json_1_1(
                value["summarization_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectProtectiveEquipmentRequest:
    out: DetectProtectiveEquipmentRequest = {}  # type: ignore[typeddict-item]
    if "Image" in data:
        import aws_sdk_rekognition.types.image

        out["image"] = aws_sdk_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("DetectProtectiveEquipmentRequest.image required")
    if "SummarizationAttributes" in data:
        import aws_sdk_rekognition.types.protective_equipment_summarization_attributes

        out["summarization_attributes"] = (
            aws_sdk_rekognition.types.protective_equipment_summarization_attributes.deserialize_aws_json_1_1(
                data["SummarizationAttributes"]
            )
        )
    return out
