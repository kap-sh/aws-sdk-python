"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#QConnectIntegrationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.arn


class QConnectIntegrationConfig(TypedDict):
    knowledge_base_arn: "aws_sdk_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: QConnectIntegrationConfig) -> dict:
    out: dict = {}
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    return out


def deserialize_json(data: dict) -> QConnectIntegrationConfig:
    out: QConnectIntegrationConfig = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError(
            "QConnectIntegrationConfig.knowledge_base_arn required"
        )
    return out
