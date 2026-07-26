"""Generated from Smithy shape ``com.amazonaws.securityagent#Authentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.authentication_provider_type


class Authentication(TypedDict, closed=True):
    provider_type: NotRequired[
        "capo_securityagent.types.authentication_provider_type.AuthenticationProviderType"
    ]
    """<p>The type of authentication provider. Valid values include SECRETS_MANAGER, AWS_LAMBDA, AWS_IAM_ROLE, and AWS_INTERNAL.</p>"""
    value: NotRequired["str"]
    """<p>The authentication value, such as a secret ARN, Lambda function ARN, or IAM role ARN, depending on the provider type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Authentication) -> dict:
    out: dict = {}
    if "provider_type" in value:
        import capo_securityagent.types.authentication_provider_type

        out["providerType"] = (
            capo_securityagent.types.authentication_provider_type.serialize_json(
                value["provider_type"]
            )
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Authentication:
    out: Authentication = {}  # type: ignore[typeddict-item]
    if "providerType" in data:
        import capo_securityagent.types.authentication_provider_type

        out["provider_type"] = (
            capo_securityagent.types.authentication_provider_type.deserialize_json(
                data["providerType"]
            )
        )
    if "value" in data:
        out["value"] = data["value"]
    return out
