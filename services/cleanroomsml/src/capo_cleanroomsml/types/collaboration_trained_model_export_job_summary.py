"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CollaborationTrainedModelExportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.status_details
    import capo_cleanroomsml.types.trained_model_arn
    import capo_cleanroomsml.types.trained_model_export_job_status
    import capo_cleanroomsml.types.trained_model_export_output_configuration
    import capo_cleanroomsml.types.uuid


class CollaborationTrainedModelExportJobSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the trained model export job was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the trained model export job was updated.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the trained model export job.</p>"""
    output_configuration: "capo_cleanroomsml.types.trained_model_export_output_configuration.TrainedModelExportOutputConfiguration"
    status: "capo_cleanroomsml.types.trained_model_export_job_status.TrainedModelExportJobStatus"
    """<p>The status of the trained model.</p>"""
    status_details: NotRequired["capo_cleanroomsml.types.status_details.StatusDetails"]
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the trained model.</p>"""
    creator_account_id: "capo_cleanroomsml.types.account_id.AccountId"
    """<p>The account ID of the member that created the trained model.</p>"""
    trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model that is being exported.</p>"""
    trained_model_version_identifier: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model that was exported in this job.</p>"""
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that created the trained model export job.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the trained model export job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationTrainedModelExportJobSummary) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types._prelude.timestamp

    out["createTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["name"] = value["name"]
    import capo_cleanroomsml.types.trained_model_export_output_configuration

    out["outputConfiguration"] = (
        capo_cleanroomsml.types.trained_model_export_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    import capo_cleanroomsml.types.trained_model_export_job_status

    out["status"] = (
        capo_cleanroomsml.types.trained_model_export_job_status.serialize_json(
            value["status"]
        )
    )
    if "status_details" in value:
        import capo_cleanroomsml.types.status_details

        out["statusDetails"] = capo_cleanroomsml.types.status_details.serialize_json(
            value["status_details"]
        )
    if "description" in value:
        out["description"] = value["description"]
    out["creatorAccountId"] = value["creator_account_id"]
    out["trainedModelArn"] = value["trained_model_arn"]
    if "trained_model_version_identifier" in value:
        out["trainedModelVersionIdentifier"] = value["trained_model_version_identifier"]
    out["membershipIdentifier"] = value["membership_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    return out


def deserialize_json(data: dict) -> CollaborationTrainedModelExportJobSummary:
    out: CollaborationTrainedModelExportJobSummary = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationTrainedModelExportJobSummary.create_time required"
        )
    if "updateTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationTrainedModelExportJobSummary.update_time required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CollaborationTrainedModelExportJobSummary.name required"
        )
    if "outputConfiguration" in data:
        import capo_cleanroomsml.types.trained_model_export_output_configuration

        out["output_configuration"] = (
            capo_cleanroomsml.types.trained_model_export_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationTrainedModelExportJobSummary.output_configuration required"
        )
    if "status" in data:
        import capo_cleanroomsml.types.trained_model_export_job_status

        out["status"] = (
            capo_cleanroomsml.types.trained_model_export_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationTrainedModelExportJobSummary.status required"
        )
    if "statusDetails" in data:
        import capo_cleanroomsml.types.status_details

        out["status_details"] = capo_cleanroomsml.types.status_details.deserialize_json(
            data["statusDetails"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "CollaborationTrainedModelExportJobSummary.creator_account_id required"
        )
    if "trainedModelArn" in data:
        out["trained_model_arn"] = data["trainedModelArn"]
    else:
        raise DeserializationError(
            "CollaborationTrainedModelExportJobSummary.trained_model_arn required"
        )
    if "trainedModelVersionIdentifier" in data:
        out["trained_model_version_identifier"] = data["trainedModelVersionIdentifier"]
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "CollaborationTrainedModelExportJobSummary.membership_identifier required"
        )
    if "collaborationIdentifier" in data:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        raise DeserializationError(
            "CollaborationTrainedModelExportJobSummary.collaboration_identifier required"
        )
    return out
