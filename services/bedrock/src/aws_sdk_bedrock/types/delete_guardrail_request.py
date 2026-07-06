"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteGuardrailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_identifier
    import aws_sdk_bedrock.types.guardrail_numerical_version


class DeleteGuardrailRequest(TypedDict, closed=True):
    guardrail_identifier: (
        "aws_sdk_bedrock.types.guardrail_identifier.GuardrailIdentifier"
    )
    """<p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>"""
    guardrail_version: NotRequired[
        "aws_sdk_bedrock.types.guardrail_numerical_version.GuardrailNumericalVersion"
    ]
    """<p>The version of the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGuardrailRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGuardrailRequest:
    out: DeleteGuardrailRequest = {}  # type: ignore[typeddict-item]
    return out
