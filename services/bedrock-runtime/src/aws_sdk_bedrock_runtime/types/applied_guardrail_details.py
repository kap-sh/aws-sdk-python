"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AppliedGuardrailDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_arn
    import aws_sdk_bedrock_runtime.types.guardrail_id
    import aws_sdk_bedrock_runtime.types.guardrail_origin_list
    import aws_sdk_bedrock_runtime.types.guardrail_ownership
    import aws_sdk_bedrock_runtime.types.guardrail_version

class AppliedGuardrailDetails(TypedDict):
    guardrail_id: NotRequired["aws_sdk_bedrock_runtime.types.guardrail_id.GuardrailId"]
    """<p>The unique ID of the guardrail that was applied.</p>"""
    guardrail_version: NotRequired["aws_sdk_bedrock_runtime.types.guardrail_version.GuardrailVersion"]
    """<p>The version of the guardrail that was applied.</p>"""
    guardrail_arn: NotRequired["aws_sdk_bedrock_runtime.types.guardrail_arn.GuardrailArn"]
    """<p>The ARN of the guardrail that was applied.</p>"""
    guardrail_origin: NotRequired["aws_sdk_bedrock_runtime.types.guardrail_origin_list.GuardrailOriginList"]
    """<p>The origin of how the guardrail was applied. This can be either requested at the API level or enforced at the account or organization level as a default guardrail.</p>"""
    guardrail_ownership: NotRequired["aws_sdk_bedrock_runtime.types.guardrail_ownership.GuardrailOwnership"]
    """<p>The ownership type of the guardrail, indicating whether it is owned by the requesting account or is a cross-account guardrail shared from another AWS account.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AppliedGuardrailDetails) -> dict:
    out: dict = {}
    if "guardrail_id" in value:
        out["guardrailId"] = value["guardrail_id"]
    if "guardrail_version" in value:
        out["guardrailVersion"] = value["guardrail_version"]
    if "guardrail_arn" in value:
        out["guardrailArn"] = value["guardrail_arn"]
    if "guardrail_origin" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_origin_list
        out["guardrailOrigin"] = aws_sdk_bedrock_runtime.types.guardrail_origin_list.serialize_json(value["guardrail_origin"])
    if "guardrail_ownership" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_ownership
        out["guardrailOwnership"] = aws_sdk_bedrock_runtime.types.guardrail_ownership.serialize_json(value["guardrail_ownership"])
    return out


def deserialize_json(data: dict) -> AppliedGuardrailDetails:
    out: AppliedGuardrailDetails = {}  # type: ignore[typeddict-item]
    if "guardrailId" in data:
        out["guardrail_id"] = data["guardrailId"]
    if "guardrailVersion" in data:
        out["guardrail_version"] = data["guardrailVersion"]
    if "guardrailArn" in data:
        out["guardrail_arn"] = data["guardrailArn"]
    if "guardrailOrigin" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_origin_list
        out["guardrail_origin"] = aws_sdk_bedrock_runtime.types.guardrail_origin_list.deserialize_json(data["guardrailOrigin"])
    if "guardrailOwnership" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_ownership
        out["guardrail_ownership"] = aws_sdk_bedrock_runtime.types.guardrail_ownership.deserialize_json(data["guardrailOwnership"])
    return out