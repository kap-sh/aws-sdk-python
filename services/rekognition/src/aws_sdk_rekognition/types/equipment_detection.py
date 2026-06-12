"""Generated from Smithy shape ``com.amazonaws.rekognition#EquipmentDetection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.bounding_box
    import aws_sdk_rekognition.types.covers_body_part
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.protective_equipment_type


class EquipmentDetection(TypedDict):
    bounding_box: NotRequired["aws_sdk_rekognition.types.bounding_box.BoundingBox"]
    """<p>A bounding box surrounding the item of detected PPE.</p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The confidence that Amazon Rekognition has that the bounding box (<code>BoundingBox</code>) contains an item of PPE.</p>"""
    type: NotRequired[
        "aws_sdk_rekognition.types.protective_equipment_type.ProtectiveEquipmentType"
    ]
    """<p>The type of detected PPE.</p>"""
    covers_body_part: NotRequired[
        "aws_sdk_rekognition.types.covers_body_part.CoversBodyPart"
    ]
    """<p>Information about the body part covered by the detected PPE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EquipmentDetection) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import aws_sdk_rekognition.types.bounding_box

        out["BoundingBox"] = (
            aws_sdk_rekognition.types.bounding_box.serialize_aws_json_1_1(
                value["bounding_box"]
            )
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "type" in value:
        import aws_sdk_rekognition.types.protective_equipment_type

        out["Type"] = (
            aws_sdk_rekognition.types.protective_equipment_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "covers_body_part" in value:
        import aws_sdk_rekognition.types.covers_body_part

        out["CoversBodyPart"] = (
            aws_sdk_rekognition.types.covers_body_part.serialize_aws_json_1_1(
                value["covers_body_part"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EquipmentDetection:
    out: EquipmentDetection = {}  # type: ignore[typeddict-item]
    if "BoundingBox" in data:
        import aws_sdk_rekognition.types.bounding_box

        out["bounding_box"] = (
            aws_sdk_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Type" in data:
        import aws_sdk_rekognition.types.protective_equipment_type

        out["type"] = (
            aws_sdk_rekognition.types.protective_equipment_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "CoversBodyPart" in data:
        import aws_sdk_rekognition.types.covers_body_part

        out["covers_body_part"] = (
            aws_sdk_rekognition.types.covers_body_part.deserialize_aws_json_1_1(
                data["CoversBodyPart"]
            )
        )
    return out
