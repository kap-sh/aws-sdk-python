"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteEnforcedGuardrailConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.account_enforced_guardrail_configuration_id


class DeleteEnforcedGuardrailConfigurationRequest(TypedDict, closed=True):
    config_id: "capo_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId"
    """<p>Unique ID for the account enforced configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnforcedGuardrailConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnforcedGuardrailConfigurationRequest:
    out: DeleteEnforcedGuardrailConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
