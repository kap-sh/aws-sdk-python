"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectProtectiveEquipmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.image
    import capo_rekognition.types.protective_equipment_summarization_attributes


class DetectProtectiveEquipmentRequest(TypedDict, closed=True):
    image: "capo_rekognition.types.image.Image"
    """<p>The image in which you want to detect PPE on detected persons. The image can be passed as image bytes or you can reference an image stored in an Amazon S3 bucket. </p>"""
    summarization_attributes: NotRequired[
        "capo_rekognition.types.protective_equipment_summarization_attributes.ProtectiveEquipmentSummarizationAttributes"
    ]
    """<p>An array of PPE types that you want to summarize.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectProtectiveEquipmentRequest) -> dict:
    out: dict = {}
    import capo_rekognition.types.image

    out["Image"] = capo_rekognition.types.image.serialize_aws_json_1_1(value["image"])
    if "summarization_attributes" in value:
        import capo_rekognition.types.protective_equipment_summarization_attributes

        out["SummarizationAttributes"] = (
            capo_rekognition.types.protective_equipment_summarization_attributes.serialize_aws_json_1_1(
                value["summarization_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectProtectiveEquipmentRequest:
    out: DetectProtectiveEquipmentRequest = {}  # type: ignore[typeddict-item]
    if "Image" in data:
        import capo_rekognition.types.image

        out["image"] = capo_rekognition.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    else:
        raise DeserializationError("DetectProtectiveEquipmentRequest.image required")
    if "SummarizationAttributes" in data:
        import capo_rekognition.types.protective_equipment_summarization_attributes

        out["summarization_attributes"] = (
            capo_rekognition.types.protective_equipment_summarization_attributes.deserialize_aws_json_1_1(
                data["SummarizationAttributes"]
            )
        )
    return out
