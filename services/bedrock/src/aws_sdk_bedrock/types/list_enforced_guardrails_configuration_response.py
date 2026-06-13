"""Generated from Smithy shape ``com.amazonaws.bedrock#ListEnforcedGuardrailsConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.account_enforced_guardrails_output_configuration
    import aws_sdk_bedrock.types.pagination_token


class ListEnforcedGuardrailsConfigurationResponse(TypedDict):
    guardrails_config: "aws_sdk_bedrock.types.account_enforced_guardrails_output_configuration.AccountEnforcedGuardrailsOutputConfiguration"
    """<p>Array of AccountEnforcedGuardrailOutputConfiguration objects.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>Opaque continuation token of previous paginated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnforcedGuardrailsConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.account_enforced_guardrails_output_configuration

    out["guardrailsConfig"] = (
        aws_sdk_bedrock.types.account_enforced_guardrails_output_configuration.serialize_json(
            value["guardrails_config"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnforcedGuardrailsConfigurationResponse:
    out: ListEnforcedGuardrailsConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "guardrailsConfig" in data:
        import aws_sdk_bedrock.types.account_enforced_guardrails_output_configuration

        out["guardrails_config"] = (
            aws_sdk_bedrock.types.account_enforced_guardrails_output_configuration.deserialize_json(
                data["guardrailsConfig"]
            )
        )
    else:
        raise DeserializationError(
            "ListEnforcedGuardrailsConfigurationResponse.guardrails_config required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
