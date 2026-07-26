"""Generated from Smithy shape ``com.amazonaws.sesv2#GetReputationEntityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.reputation_entity


class GetReputationEntityResponse(TypedDict, closed=True):
    reputation_entity: NotRequired[
        "capo_sesv2.types.reputation_entity.ReputationEntity"
    ]
    """<p>The reputation entity information, including status records, policy configuration, and reputation impact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReputationEntityResponse) -> dict:
    out: dict = {}
    if "reputation_entity" in value:
        import capo_sesv2.types.reputation_entity

        out["ReputationEntity"] = capo_sesv2.types.reputation_entity.serialize_json(
            value["reputation_entity"]
        )
    return out


def deserialize_json(data: dict) -> GetReputationEntityResponse:
    out: GetReputationEntityResponse = {}  # type: ignore[typeddict-item]
    if "ReputationEntity" in data:
        import capo_sesv2.types.reputation_entity

        out["reputation_entity"] = capo_sesv2.types.reputation_entity.deserialize_json(
            data["ReputationEntity"]
        )
    return out
