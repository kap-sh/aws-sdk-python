"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectEnvironmentRegistryCredential``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsCodeBuildProjectEnvironmentRegistryCredential(TypedDict):
    credential: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN or name of credentials created using Secrets Manager.</p> <note> <p>The credential can use the name of the credentials only if they exist in your current Amazon Web Services Region. </p> </note>"""
    credential_provider: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The service that created the credentials to access a private Docker registry.</p> <p>The valid value,<code> SECRETS_MANAGER</code>, is for Secrets Manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectEnvironmentRegistryCredential) -> dict:
    out: dict = {}
    if "credential" in value:
        out["Credential"] = value["credential"]
    if "credential_provider" in value:
        out["CredentialProvider"] = value["credential_provider"]
    return out


def deserialize_json(data: dict) -> AwsCodeBuildProjectEnvironmentRegistryCredential:
    out: AwsCodeBuildProjectEnvironmentRegistryCredential = {}  # type: ignore[typeddict-item]
    if "Credential" in data:
        out["credential"] = data["Credential"]
    if "CredentialProvider" in data:
        out["credential_provider"] = data["CredentialProvider"]
    return out
