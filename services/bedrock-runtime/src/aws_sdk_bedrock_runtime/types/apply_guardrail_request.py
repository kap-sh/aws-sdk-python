"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ApplyGuardrailRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_content_block_list
    import aws_sdk_bedrock_runtime.types.guardrail_content_source
    import aws_sdk_bedrock_runtime.types.guardrail_identifier
    import aws_sdk_bedrock_runtime.types.guardrail_output_scope
    import aws_sdk_bedrock_runtime.types.guardrail_version


class ApplyGuardrailRequest(TypedDict):
    guardrail_identifier: (
        "aws_sdk_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier"
    )
    """<p>The guardrail identifier used in the request to apply the guardrail.</p>"""
    guardrail_version: (
        "aws_sdk_bedrock_runtime.types.guardrail_version.GuardrailVersion"
    )
    """<p>The guardrail version used in the request to apply the guardrail.</p>"""
    source: (
        "aws_sdk_bedrock_runtime.types.guardrail_content_source.GuardrailContentSource"
    )
    """<p>The source of data used in the request to apply the guardrail.</p>"""
    content: "aws_sdk_bedrock_runtime.types.guardrail_content_block_list.GuardrailContentBlockList"
    """<p>The content details used in the request to apply the guardrail.</p>"""
    output_scope: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_output_scope.GuardrailOutputScope"
    ]
    """<p>Specifies the scope of the output that you get in the response. Set to <code>FULL</code> to return the entire output, including any detected and non-detected entries in the response for enhanced debugging.</p> <p>Note that the full output scope doesn't apply to word filters or regex in sensitive information filters. It does apply to all other filtering policies, including sensitive information with filters that can detect personally identifiable information (PII).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplyGuardrailRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.guardrail_content_source

    out["source"] = (
        aws_sdk_bedrock_runtime.types.guardrail_content_source.serialize_json(
            value["source"]
        )
    )
    import aws_sdk_bedrock_runtime.types.guardrail_content_block_list

    out["content"] = (
        aws_sdk_bedrock_runtime.types.guardrail_content_block_list.serialize_json(
            value["content"]
        )
    )
    if "output_scope" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_output_scope

        out["outputScope"] = (
            aws_sdk_bedrock_runtime.types.guardrail_output_scope.serialize_json(
                value["output_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApplyGuardrailRequest:
    out: ApplyGuardrailRequest = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_content_source

        out["source"] = (
            aws_sdk_bedrock_runtime.types.guardrail_content_source.deserialize_json(
                data["source"]
            )
        )
    else:
        raise DeserializationError("ApplyGuardrailRequest.source required")
    if "content" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_content_block_list

        out["content"] = (
            aws_sdk_bedrock_runtime.types.guardrail_content_block_list.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("ApplyGuardrailRequest.content required")
    if "outputScope" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_output_scope

        out["output_scope"] = (
            aws_sdk_bedrock_runtime.types.guardrail_output_scope.deserialize_json(
                data["outputScope"]
            )
        )
    return out
