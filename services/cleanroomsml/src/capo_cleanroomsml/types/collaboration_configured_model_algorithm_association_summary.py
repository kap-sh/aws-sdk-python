"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CollaborationConfiguredModelAlgorithmAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.configured_model_algorithm_arn
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.uuid


class CollaborationConfiguredModelAlgorithmAssociationSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the configured model algorithm association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured model algorithm association was updated.</p>"""
    configured_model_algorithm_association_arn: "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the configured model algorithm association.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured model algorithm association.</p>"""
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that created the configured model algorithm association.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the configured model algorithm association.</p>"""
    configured_model_algorithm_arn: "capo_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm that is associated to the collaboration.</p>"""
    creator_account_id: "capo_cleanroomsml.types.account_id.AccountId"
    """<p>The account ID of the member that created the configured model algorithm association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: CollaborationConfiguredModelAlgorithmAssociationSummary,
) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types._prelude.timestamp

    out["createTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["configuredModelAlgorithmAssociationArn"] = value[
        "configured_model_algorithm_association_arn"
    ]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["membershipIdentifier"] = value["membership_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    out["configuredModelAlgorithmArn"] = value["configured_model_algorithm_arn"]
    out["creatorAccountId"] = value["creator_account_id"]
    return out


def deserialize_json(
    data: dict,
) -> CollaborationConfiguredModelAlgorithmAssociationSummary:
    out: CollaborationConfiguredModelAlgorithmAssociationSummary = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationConfiguredModelAlgorithmAssociationSummary.create_time required"
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
            "CollaborationConfiguredModelAlgorithmAssociationSummary.update_time required"
        )
    if "configuredModelAlgorithmAssociationArn" in data:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    else:
        raise DeserializationError(
            "CollaborationConfiguredModelAlgorithmAssociationSummary.configured_model_algorithm_association_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredModelAlgorithmAssociationSummary.name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredModelAlgorithmAssociationSummary.membership_identifier required"
        )
    if "collaborationIdentifier" in data:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredModelAlgorithmAssociationSummary.collaboration_identifier required"
        )
    if "configuredModelAlgorithmArn" in data:
        out["configured_model_algorithm_arn"] = data["configuredModelAlgorithmArn"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredModelAlgorithmAssociationSummary.configured_model_algorithm_arn required"
        )
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "CollaborationConfiguredModelAlgorithmAssociationSummary.creator_account_id required"
        )
    return out
