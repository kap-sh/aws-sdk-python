"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectProtectiveEquipmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.protective_equipment_persons
    import capo_rekognition.types.protective_equipment_summary
    import capo_rekognition.types.string


class DetectProtectiveEquipmentResponse(TypedDict, closed=True):
    protective_equipment_model_version: NotRequired[
        "capo_rekognition.types.string.String"
    ]
    """<p>The version number of the PPE detection model used to detect PPE in the image.</p>"""
    persons: NotRequired[
        "capo_rekognition.types.protective_equipment_persons.ProtectiveEquipmentPersons"
    ]
    """<p>An array of persons detected in the image (including persons not wearing PPE).</p>"""
    summary: NotRequired[
        "capo_rekognition.types.protective_equipment_summary.ProtectiveEquipmentSummary"
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
        import capo_rekognition.types.protective_equipment_persons

        out["Persons"] = (
            capo_rekognition.types.protective_equipment_persons.serialize_aws_json_1_1(
                value["persons"]
            )
        )
    if "summary" in value:
        import capo_rekognition.types.protective_equipment_summary

        out["Summary"] = (
            capo_rekognition.types.protective_equipment_summary.serialize_aws_json_1_1(
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
        import capo_rekognition.types.protective_equipment_persons

        out["persons"] = (
            capo_rekognition.types.protective_equipment_persons.deserialize_aws_json_1_1(
                data["Persons"]
            )
        )
    if "Summary" in data:
        import capo_rekognition.types.protective_equipment_summary

        out["summary"] = (
            capo_rekognition.types.protective_equipment_summary.deserialize_aws_json_1_1(
                data["Summary"]
            )
        )
    return out
