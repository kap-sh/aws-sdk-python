"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteEnforcedGuardrailConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id


class DeleteEnforcedGuardrailConfigurationRequest(TypedDict):
    config_id: "aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId"
    """<p>Unique ID for the account enforced configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnforcedGuardrailConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnforcedGuardrailConfigurationRequest:
    out: DeleteEnforcedGuardrailConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
