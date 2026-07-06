"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#QConnectIntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.arn


class QConnectIntegrationSummary(TypedDict, closed=True):
    knowledge_base_arn: "aws_sdk_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: QConnectIntegrationSummary) -> dict:
    out: dict = {}
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    return out


def deserialize_json(data: dict) -> QConnectIntegrationSummary:
    out: QConnectIntegrationSummary = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError(
            "QConnectIntegrationSummary.knowledge_base_arn required"
        )
    return out
