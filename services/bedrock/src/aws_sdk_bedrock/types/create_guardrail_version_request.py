"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateGuardrailVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_description
    import aws_sdk_bedrock.types.guardrail_identifier
    import aws_sdk_bedrock.types.idempotency_token


class CreateGuardrailVersionRequest(TypedDict):
    guardrail_identifier: (
        "aws_sdk_bedrock.types.guardrail_identifier.GuardrailIdentifier"
    )
    """<p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.guardrail_description.GuardrailDescription"
    ]
    """<p>A description of the guardrail version.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon S3 User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGuardrailVersionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateGuardrailVersionRequest:
    out: CreateGuardrailVersionRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
