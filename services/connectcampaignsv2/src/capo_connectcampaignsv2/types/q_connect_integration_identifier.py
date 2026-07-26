"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#QConnectIntegrationIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn


class QConnectIntegrationIdentifier(TypedDict, closed=True):
    knowledge_base_arn: "capo_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: QConnectIntegrationIdentifier) -> dict:
    out: dict = {}
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    return out


def deserialize_json(data: dict) -> QConnectIntegrationIdentifier:
    out: QConnectIntegrationIdentifier = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError(
            "QConnectIntegrationIdentifier.knowledge_base_arn required"
        )
    return out
