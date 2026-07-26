"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListConfiguredModelAlgorithmAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_model_algorithm_association_list
    import capo_cleanroomsml.types.next_token


class ListConfiguredModelAlgorithmAssociationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    configured_model_algorithm_associations: "capo_cleanroomsml.types.configured_model_algorithm_association_list.ConfiguredModelAlgorithmAssociationList"
    """<p>The list of configured model algorithm associations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfiguredModelAlgorithmAssociationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.configured_model_algorithm_association_list

    out["configuredModelAlgorithmAssociations"] = (
        capo_cleanroomsml.types.configured_model_algorithm_association_list.serialize_json(
            value["configured_model_algorithm_associations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListConfiguredModelAlgorithmAssociationsResponse:
    out: ListConfiguredModelAlgorithmAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "configuredModelAlgorithmAssociations" in data:
        import capo_cleanroomsml.types.configured_model_algorithm_association_list

        out["configured_model_algorithm_associations"] = (
            capo_cleanroomsml.types.configured_model_algorithm_association_list.deserialize_json(
                data["configuredModelAlgorithmAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "ListConfiguredModelAlgorithmAssociationsResponse.configured_model_algorithm_associations required"
        )
    return out
