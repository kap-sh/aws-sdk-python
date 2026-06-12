"""Generated from Smithy shape ``com.amazonaws.bedrock#PutEnforcedGuardrailConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id
    import aws_sdk_bedrock.types.timestamp


class PutEnforcedGuardrailConfigurationResponse(TypedDict):
    config_id: NotRequired[
        "aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId"
    ]
    """<p>Unique ID for the account enforced configuration.</p>"""
    updated_at: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Timestamp.</p>"""
    updated_by: NotRequired["str"]
    """<p>The ARN of the role used to update the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEnforcedGuardrailConfigurationResponse) -> dict:
    out: dict = {}
    if "config_id" in value:
        out["configId"] = value["config_id"]
    if "updated_at" in value:
        import aws_sdk_bedrock.types.timestamp

        out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> PutEnforcedGuardrailConfigurationResponse:
    out: PutEnforcedGuardrailConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "configId" in data:
        out["config_id"] = data["configId"]
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out
