"""Generated from Smithy shape ``com.amazonaws.bedrock#GetGuardrailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_identifier
    import aws_sdk_bedrock.types.guardrail_version


class GetGuardrailRequest(TypedDict, closed=True):
    guardrail_identifier: (
        "aws_sdk_bedrock.types.guardrail_identifier.GuardrailIdentifier"
    )
    """<p>The unique identifier of the guardrail for which to get details. This can be an ID or the ARN.</p>"""
    guardrail_version: NotRequired[
        "aws_sdk_bedrock.types.guardrail_version.GuardrailVersion"
    ]
    """<p>The version of the guardrail for which to get details. If you don't specify a version, the response returns details for the <code>DRAFT</code> version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGuardrailRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGuardrailRequest:
    out: GetGuardrailRequest = {}  # type: ignore[typeddict-item]
    return out
