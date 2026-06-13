"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetCollaborationConfiguredModelAlgorithmAssociationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.account_id
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_arn
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.privacy_configuration
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.uuid


class GetCollaborationConfiguredModelAlgorithmAssociationResponse(TypedDict):
    create_time: "datetime.datetime"
    """<p>The time at which the configured model algorithm association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured model algorithm association was updated.</p>"""
    configured_model_algorithm_association_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association.</p>"""
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that created the configured model algorithm association.</p>"""
    collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the configured model algorithm association.</p>"""
    configured_model_algorithm_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the configured model algorithm association.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured model algorithm association.</p>"""
    creator_account_id: "aws_sdk_cleanroomsml.types.account_id.AccountId"
    """<p>The account ID of the member that created the configured model algorithm association.</p>"""
    privacy_configuration: NotRequired[
        "aws_sdk_cleanroomsml.types.privacy_configuration.PrivacyConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(
    value: GetCollaborationConfiguredModelAlgorithmAssociationResponse,
) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["configuredModelAlgorithmAssociationArn"] = value[
        "configured_model_algorithm_association_arn"
    ]
    out["membershipIdentifier"] = value["membership_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    out["configuredModelAlgorithmArn"] = value["configured_model_algorithm_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["creatorAccountId"] = value["creator_account_id"]
    if "privacy_configuration" in value:
        import aws_sdk_cleanroomsml.types.privacy_configuration

        out["privacyConfiguration"] = (
            aws_sdk_cleanroomsml.types.privacy_configuration.serialize_json(
                value["privacy_configuration"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> GetCollaborationConfiguredModelAlgorithmAssociationResponse:
    out: GetCollaborationConfiguredModelAlgorithmAssociationResponse = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationConfiguredModelAlgorithmAssociationResponse.create_time required"
        )
    if "updateTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationConfiguredModelAlgorithmAssociationResponse.update_time required"
        )
    if "configuredModelAlgorithmAssociationArn" in data:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    else:
        raise DeserializationError(
            "GetCollaborationConfiguredModelAlgorithmAssociationResponse.configured_model_algorithm_association_arn required"
        )
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "GetCollaborationConfiguredModelAlgorithmAssociationResponse.membership_identifier required"
        )
    if "collaborationIdentifier" in data:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        raise DeserializationError(
            "GetCollaborationConfiguredModelAlgorithmAssociationResponse.collaboration_identifier required"
        )
    if "configuredModelAlgorithmArn" in data:
        out["configured_model_algorithm_arn"] = data["configuredModelAlgorithmArn"]
    else:
        raise DeserializationError(
            "GetCollaborationConfiguredModelAlgorithmAssociationResponse.configured_model_algorithm_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "GetCollaborationConfiguredModelAlgorithmAssociationResponse.name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "GetCollaborationConfiguredModelAlgorithmAssociationResponse.creator_account_id required"
        )
    if "privacyConfiguration" in data:
        import aws_sdk_cleanroomsml.types.privacy_configuration

        out["privacy_configuration"] = (
            aws_sdk_cleanroomsml.types.privacy_configuration.deserialize_json(
                data["privacyConfiguration"]
            )
        )
    return out
