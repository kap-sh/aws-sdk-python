"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn
    import capo_cleanroomsml.types.incremental_training_data_channels_output
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.trained_model_arn
    import capo_cleanroomsml.types.trained_model_status
    import capo_cleanroomsml.types.uuid


class TrainedModelSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the trained model was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the trained model was updated.</p>"""
    trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model.</p>"""
    version_identifier: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of this trained model version.</p>"""
    incremental_training_data_channels: NotRequired[
        "capo_cleanroomsml.types.incremental_training_data_channels_output.IncrementalTrainingDataChannelsOutput"
    ]
    """<p>Information about the incremental training data channels used to create this version of the trained model.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the trained model.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the trained model.</p>"""
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that created the trained model.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the trained model.</p>"""
    status: "capo_cleanroomsml.types.trained_model_status.TrainedModelStatus"
    """<p>The status of the trained model.</p>"""
    configured_model_algorithm_association_arn: "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association that was used to create this trained model.</p>"""
    ml_model_training_payer_account_id: NotRequired[
        "capo_cleanroomsml.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that is responsible for paying for model training costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelSummary) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types._prelude.timestamp

    out["createTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["trainedModelArn"] = value["trained_model_arn"]
    if "version_identifier" in value:
        out["versionIdentifier"] = value["version_identifier"]
    if "incremental_training_data_channels" in value:
        import capo_cleanroomsml.types.incremental_training_data_channels_output

        out["incrementalTrainingDataChannels"] = (
            capo_cleanroomsml.types.incremental_training_data_channels_output.serialize_json(
                value["incremental_training_data_channels"]
            )
        )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["membershipIdentifier"] = value["membership_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    import capo_cleanroomsml.types.trained_model_status

    out["status"] = capo_cleanroomsml.types.trained_model_status.serialize_json(
        value["status"]
    )
    out["configuredModelAlgorithmAssociationArn"] = value[
        "configured_model_algorithm_association_arn"
    ]
    if "ml_model_training_payer_account_id" in value:
        out["mlModelTrainingPayerAccountId"] = value[
            "ml_model_training_payer_account_id"
        ]
    return out


def deserialize_json(data: dict) -> TrainedModelSummary:
    out: TrainedModelSummary = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("TrainedModelSummary.create_time required")
    if "updateTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("TrainedModelSummary.update_time required")
    if "trainedModelArn" in data:
        out["trained_model_arn"] = data["trainedModelArn"]
    else:
        raise DeserializationError("TrainedModelSummary.trained_model_arn required")
    if "versionIdentifier" in data:
        out["version_identifier"] = data["versionIdentifier"]
    if "incrementalTrainingDataChannels" in data:
        import capo_cleanroomsml.types.incremental_training_data_channels_output

        out["incremental_training_data_channels"] = (
            capo_cleanroomsml.types.incremental_training_data_channels_output.deserialize_json(
                data["incrementalTrainingDataChannels"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TrainedModelSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError("TrainedModelSummary.membership_identifier required")
    if "collaborationIdentifier" in data:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        raise DeserializationError(
            "TrainedModelSummary.collaboration_identifier required"
        )
    if "status" in data:
        import capo_cleanroomsml.types.trained_model_status

        out["status"] = capo_cleanroomsml.types.trained_model_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("TrainedModelSummary.status required")
    if "configuredModelAlgorithmAssociationArn" in data:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    else:
        raise DeserializationError(
            "TrainedModelSummary.configured_model_algorithm_association_arn required"
        )
    if "mlModelTrainingPayerAccountId" in data:
        out["ml_model_training_payer_account_id"] = data[
            "mlModelTrainingPayerAccountId"
        ]
    return out
