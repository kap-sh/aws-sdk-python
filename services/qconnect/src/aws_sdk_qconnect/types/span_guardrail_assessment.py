"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanGuardrailAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.guardrail_action
    import aws_sdk_qconnect.types.guardrail_policy_result_list
    import aws_sdk_qconnect.types.guardrail_source
    import aws_sdk_qconnect.types.non_empty_string


class SpanGuardrailAssessment(TypedDict, closed=True):
    guardrail_id: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>Unique AI Guardrail identifier.</p>"""
    guardrail_name: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>Customer-defined display name of the AI Guardrail resource.</p>"""
    source: "aws_sdk_qconnect.types.guardrail_source.GuardrailSource"
    """<p>Content source the guardrail was evaluated against.</p>"""
    action: "aws_sdk_qconnect.types.guardrail_action.GuardrailAction"
    """<p>Outcome of the guardrail assessment.</p>"""
    policies: NotRequired[
        "aws_sdk_qconnect.types.guardrail_policy_result_list.GuardrailPolicyResultList"
    ]
    """<p>Per-policy assessment results. Absent or empty when action is NONE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanGuardrailAssessment) -> dict:
    out: dict = {}
    out["guardrailId"] = value["guardrail_id"]
    out["guardrailName"] = value["guardrail_name"]
    out["source"] = value["source"]
    out["action"] = value["action"]
    if "policies" in value:
        import aws_sdk_qconnect.types.guardrail_policy_result_list

        out["policies"] = (
            aws_sdk_qconnect.types.guardrail_policy_result_list.serialize_json(
                value["policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> SpanGuardrailAssessment:
    out: SpanGuardrailAssessment = {}  # type: ignore[typeddict-item]
    if "guardrailId" in data:
        out["guardrail_id"] = data["guardrailId"]
    else:
        raise DeserializationError("SpanGuardrailAssessment.guardrail_id required")
    if "guardrailName" in data:
        out["guardrail_name"] = data["guardrailName"]
    else:
        raise DeserializationError("SpanGuardrailAssessment.guardrail_name required")
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("SpanGuardrailAssessment.source required")
    if "action" in data:
        out["action"] = data["action"]
    else:
        raise DeserializationError("SpanGuardrailAssessment.action required")
    if "policies" in data:
        import aws_sdk_qconnect.types.guardrail_policy_result_list

        out["policies"] = (
            aws_sdk_qconnect.types.guardrail_policy_result_list.deserialize_json(
                data["policies"]
            )
        )
    return out
