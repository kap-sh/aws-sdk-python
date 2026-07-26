"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DeleteConfiguredModelAlgorithmAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn
    import capo_cleanroomsml.types.uuid


class DeleteConfiguredModelAlgorithmAssociationRequest(TypedDict, closed=True):
    configured_model_algorithm_association_arn: "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association that you want to delete.</p>"""
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that is deleting the configured model algorithm association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfiguredModelAlgorithmAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfiguredModelAlgorithmAssociationRequest:
    out: DeleteConfiguredModelAlgorithmAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
