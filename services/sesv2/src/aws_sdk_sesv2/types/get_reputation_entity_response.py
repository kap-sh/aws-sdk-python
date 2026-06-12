"""Generated from Smithy shape ``com.amazonaws.sesv2#GetReputationEntityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.reputation_entity


class GetReputationEntityResponse(TypedDict):
    reputation_entity: NotRequired[
        "aws_sdk_sesv2.types.reputation_entity.ReputationEntity"
    ]
    """<p>The reputation entity information, including status records, policy configuration, and reputation impact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReputationEntityResponse) -> dict:
    out: dict = {}
    if "reputation_entity" in value:
        import aws_sdk_sesv2.types.reputation_entity

        out["ReputationEntity"] = aws_sdk_sesv2.types.reputation_entity.serialize_json(
            value["reputation_entity"]
        )
    return out


def deserialize_json(data: dict) -> GetReputationEntityResponse:
    out: GetReputationEntityResponse = {}  # type: ignore[typeddict-item]
    if "ReputationEntity" in data:
        import aws_sdk_sesv2.types.reputation_entity

        out["reputation_entity"] = (
            aws_sdk_sesv2.types.reputation_entity.deserialize_json(
                data["ReputationEntity"]
            )
        )
    return out
