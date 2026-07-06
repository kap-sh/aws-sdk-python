"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailContentPolicyAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_list


class GuardrailContentPolicyAssessment(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_list.GuardrailContentFilterList"
    ]
    """<p>The filter details of the policy assessment used in the Guardrails filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentPolicyAssessment) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_list

        out["filters"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_list.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailContentPolicyAssessment:
    out: GuardrailContentPolicyAssessment = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_list

        out["filters"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter_list.deserialize_json(
                data["filters"]
            )
        )
    return out
