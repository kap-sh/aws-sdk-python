"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectProtectiveEquipmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.protective_equipment_persons
    import aws_sdk_rekognition.types.protective_equipment_summary
    import aws_sdk_rekognition.types.string


class DetectProtectiveEquipmentResponse(TypedDict):
    protective_equipment_model_version: NotRequired[
        "aws_sdk_rekognition.types.string.String"
    ]
    """<p>The version number of the PPE detection model used to detect PPE in the image.</p>"""
    persons: NotRequired[
        "aws_sdk_rekognition.types.protective_equipment_persons.ProtectiveEquipmentPersons"
    ]
    """<p>An array of persons detected in the image (including persons not wearing PPE).</p>"""
    summary: NotRequired[
        "aws_sdk_rekognition.types.protective_equipment_summary.ProtectiveEquipmentSummary"
    ]
    """<p>Summary information for the types of PPE specified in the <code>SummarizationAttributes</code> input parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectProtectiveEquipmentResponse) -> dict:
    out: dict = {}
    if "protective_equipment_model_version" in value:
        out["ProtectiveEquipmentModelVersion"] = value[
            "protective_equipment_model_version"
        ]
    if "persons" in value:
        import aws_sdk_rekognition.types.protective_equipment_persons

        out["Persons"] = (
            aws_sdk_rekognition.types.protective_equipment_persons.serialize_aws_json_1_1(
                value["persons"]
            )
        )
    if "summary" in value:
        import aws_sdk_rekognition.types.protective_equipment_summary

        out["Summary"] = (
            aws_sdk_rekognition.types.protective_equipment_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectProtectiveEquipmentResponse:
    out: DetectProtectiveEquipmentResponse = {}  # type: ignore[typeddict-item]
    if "ProtectiveEquipmentModelVersion" in data:
        out["protective_equipment_model_version"] = data[
            "ProtectiveEquipmentModelVersion"
        ]
    if "Persons" in data:
        import aws_sdk_rekognition.types.protective_equipment_persons

        out["persons"] = (
            aws_sdk_rekognition.types.protective_equipment_persons.deserialize_aws_json_1_1(
                data["Persons"]
            )
        )
    if "Summary" in data:
        import aws_sdk_rekognition.types.protective_equipment_summary

        out["summary"] = (
            aws_sdk_rekognition.types.protective_equipment_summary.deserialize_aws_json_1_1(
                data["Summary"]
            )
        )
    return out
