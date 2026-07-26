"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailPolicyResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_policy_result

GuardrailPolicyResultList: TypeAlias = list[
    "capo_qconnect.types.guardrail_policy_result.GuardrailPolicyResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPolicyResultList) -> list:
    import capo_qconnect.types.guardrail_policy_result

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.guardrail_policy_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailPolicyResultList:
    import capo_qconnect.types.guardrail_policy_result

    out: GuardrailPolicyResultList = []
    for item in data:
        out.append(capo_qconnect.types.guardrail_policy_result.deserialize_json(item))
    return out
