"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AppliedGuardrailDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_arn
    import capo_bedrock_runtime.types.guardrail_id
    import capo_bedrock_runtime.types.guardrail_origin_list
    import capo_bedrock_runtime.types.guardrail_ownership
    import capo_bedrock_runtime.types.guardrail_version


class AppliedGuardrailDetails(TypedDict, closed=True):
    guardrail_id: NotRequired["capo_bedrock_runtime.types.guardrail_id.GuardrailId"]
    """<p>The unique ID of the guardrail that was applied.</p>"""
    guardrail_version: NotRequired[
        "capo_bedrock_runtime.types.guardrail_version.GuardrailVersion"
    ]
    """<p>The version of the guardrail that was applied.</p>"""
    guardrail_arn: NotRequired["capo_bedrock_runtime.types.guardrail_arn.GuardrailArn"]
    """<p>The ARN of the guardrail that was applied.</p>"""
    guardrail_origin: NotRequired[
        "capo_bedrock_runtime.types.guardrail_origin_list.GuardrailOriginList"
    ]
    """<p>The origin of how the guardrail was applied. This can be either requested at the API level or enforced at the account or organization level as a default guardrail.</p>"""
    guardrail_ownership: NotRequired[
        "capo_bedrock_runtime.types.guardrail_ownership.GuardrailOwnership"
    ]
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
        import capo_bedrock_runtime.types.guardrail_origin_list

        out["guardrailOrigin"] = (
            capo_bedrock_runtime.types.guardrail_origin_list.serialize_json(
                value["guardrail_origin"]
            )
        )
    if "guardrail_ownership" in value:
        import capo_bedrock_runtime.types.guardrail_ownership

        out["guardrailOwnership"] = (
            capo_bedrock_runtime.types.guardrail_ownership.serialize_json(
                value["guardrail_ownership"]
            )
        )
    return out


def deserialize_json(data: dict) -> AppliedGuardrailDetails:
    out: AppliedGuardrailDetails = {}  # type: ignore[typeddict-item]
    if data.get("guardrailId") is not None:
        out["guardrail_id"] = data["guardrailId"]
    if data.get("guardrailVersion") is not None:
        out["guardrail_version"] = data["guardrailVersion"]
    if data.get("guardrailArn") is not None:
        out["guardrail_arn"] = data["guardrailArn"]
    if data.get("guardrailOrigin") is not None:
        import capo_bedrock_runtime.types.guardrail_origin_list

        out["guardrail_origin"] = (
            capo_bedrock_runtime.types.guardrail_origin_list.deserialize_json(
                data["guardrailOrigin"]
            )
        )
    if data.get("guardrailOwnership") is not None:
        import capo_bedrock_runtime.types.guardrail_ownership

        out["guardrail_ownership"] = (
            capo_bedrock_runtime.types.guardrail_ownership.deserialize_json(
                data["guardrailOwnership"]
            )
        )
    return out
