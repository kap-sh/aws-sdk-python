"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationConfiguredModelAlgorithmAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.collaboration_configured_model_algorithm_association_list
    import aws_sdk_cleanroomsml.types.next_token


class ListCollaborationConfiguredModelAlgorithmAssociationsResponse(
    TypedDict, closed=True
):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    collaboration_configured_model_algorithm_associations: "aws_sdk_cleanroomsml.types.collaboration_configured_model_algorithm_association_list.CollaborationConfiguredModelAlgorithmAssociationList"
    """<p>The configured model algorithm associations that belong to this collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: ListCollaborationConfiguredModelAlgorithmAssociationsResponse,
) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.collaboration_configured_model_algorithm_association_list

    out["collaborationConfiguredModelAlgorithmAssociations"] = (
        aws_sdk_cleanroomsml.types.collaboration_configured_model_algorithm_association_list.serialize_json(
            value["collaboration_configured_model_algorithm_associations"]
        )
    )
    return out


def deserialize_json(
    data: dict,
) -> ListCollaborationConfiguredModelAlgorithmAssociationsResponse:
    out: ListCollaborationConfiguredModelAlgorithmAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "collaborationConfiguredModelAlgorithmAssociations" in data:
        import aws_sdk_cleanroomsml.types.collaboration_configured_model_algorithm_association_list

        out["collaboration_configured_model_algorithm_associations"] = (
            aws_sdk_cleanroomsml.types.collaboration_configured_model_algorithm_association_list.deserialize_json(
                data["collaborationConfiguredModelAlgorithmAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "ListCollaborationConfiguredModelAlgorithmAssociationsResponse.collaboration_configured_model_algorithm_associations required"
        )
    return out
