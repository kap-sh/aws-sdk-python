"""Generated from Smithy shape ``com.amazonaws.rekognition#ProtectiveEquipmentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.protective_equipment_person_ids


class ProtectiveEquipmentSummary(TypedDict):
    persons_with_required_equipment: NotRequired[
        "aws_sdk_rekognition.types.protective_equipment_person_ids.ProtectiveEquipmentPersonIds"
    ]
    """<p>An array of IDs for persons who are wearing detected personal protective equipment. </p>"""
    persons_without_required_equipment: NotRequired[
        "aws_sdk_rekognition.types.protective_equipment_person_ids.ProtectiveEquipmentPersonIds"
    ]
    """<p>An array of IDs for persons who are not wearing all of the types of PPE specified in the <code>RequiredEquipmentTypes</code> field of the detected personal protective equipment. </p>"""
    persons_indeterminate: NotRequired[
        "aws_sdk_rekognition.types.protective_equipment_person_ids.ProtectiveEquipmentPersonIds"
    ]
    """<p>An array of IDs for persons where it was not possible to determine if they are wearing personal protective equipment. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectiveEquipmentSummary) -> dict:
    out: dict = {}
    if "persons_with_required_equipment" in value:
        import aws_sdk_rekognition.types.protective_equipment_person_ids

        out["PersonsWithRequiredEquipment"] = (
            aws_sdk_rekognition.types.protective_equipment_person_ids.serialize_aws_json_1_1(
                value["persons_with_required_equipment"]
            )
        )
    if "persons_without_required_equipment" in value:
        import aws_sdk_rekognition.types.protective_equipment_person_ids

        out["PersonsWithoutRequiredEquipment"] = (
            aws_sdk_rekognition.types.protective_equipment_person_ids.serialize_aws_json_1_1(
                value["persons_without_required_equipment"]
            )
        )
    if "persons_indeterminate" in value:
        import aws_sdk_rekognition.types.protective_equipment_person_ids

        out["PersonsIndeterminate"] = (
            aws_sdk_rekognition.types.protective_equipment_person_ids.serialize_aws_json_1_1(
                value["persons_indeterminate"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectiveEquipmentSummary:
    out: ProtectiveEquipmentSummary = {}  # type: ignore[typeddict-item]
    if "PersonsWithRequiredEquipment" in data:
        import aws_sdk_rekognition.types.protective_equipment_person_ids

        out["persons_with_required_equipment"] = (
            aws_sdk_rekognition.types.protective_equipment_person_ids.deserialize_aws_json_1_1(
                data["PersonsWithRequiredEquipment"]
            )
        )
    if "PersonsWithoutRequiredEquipment" in data:
        import aws_sdk_rekognition.types.protective_equipment_person_ids

        out["persons_without_required_equipment"] = (
            aws_sdk_rekognition.types.protective_equipment_person_ids.deserialize_aws_json_1_1(
                data["PersonsWithoutRequiredEquipment"]
            )
        )
    if "PersonsIndeterminate" in data:
        import aws_sdk_rekognition.types.protective_equipment_person_ids

        out["persons_indeterminate"] = (
            aws_sdk_rekognition.types.protective_equipment_person_ids.deserialize_aws_json_1_1(
                data["PersonsIndeterminate"]
            )
        )
    return out
