"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentPolicyAssessment``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_content_filter_list


class GuardrailContentPolicyAssessment(TypedDict):
    filters: "aws_sdk_bedrock_runtime.types.guardrail_content_filter_list.GuardrailContentFilterList"
    """<p>The content policy filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentPolicyAssessment) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.guardrail_content_filter_list

    out["filters"] = (
        aws_sdk_bedrock_runtime.types.guardrail_content_filter_list.serialize_json(
            value["filters"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailContentPolicyAssessment:
    out: GuardrailContentPolicyAssessment = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_content_filter_list

        out["filters"] = (
            aws_sdk_bedrock_runtime.types.guardrail_content_filter_list.deserialize_json(
                data["filters"]
            )
        )
    else:
        raise DeserializationError("GuardrailContentPolicyAssessment.filters required")
    return out
