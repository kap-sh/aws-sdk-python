"""Generated from Smithy shape ``com.amazonaws.qbusiness#SamlProviderConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.saml_authentication_url


class SamlProviderConfiguration(TypedDict):
    authentication_url: (
        "aws_sdk_qbusiness.types.saml_authentication_url.SamlAuthenticationUrl"
    )
    """<p>The URL where Amazon Q Business end users will be redirected for authentication. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamlProviderConfiguration) -> dict:
    out: dict = {}
    out["authenticationUrl"] = value["authentication_url"]
    return out


def deserialize_json(data: dict) -> SamlProviderConfiguration:
    out: SamlProviderConfiguration = {}  # type: ignore[typeddict-item]
    if "authenticationUrl" in data:
        out["authentication_url"] = data["authenticationUrl"]
    else:
        raise DeserializationError(
            "SamlProviderConfiguration.authentication_url required"
        )
    return out
