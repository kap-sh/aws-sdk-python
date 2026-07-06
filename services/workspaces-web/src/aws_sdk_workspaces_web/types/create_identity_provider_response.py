"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateIdentityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.subresource_arn


class CreateIdentityProviderResponse(TypedDict, closed=True):
    identity_provider_arn: "aws_sdk_workspaces_web.types.subresource_arn.SubresourceARN"
    """<p>The ARN of the identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIdentityProviderResponse) -> dict:
    out: dict = {}
    out["identityProviderArn"] = value["identity_provider_arn"]
    return out


def deserialize_json(data: dict) -> CreateIdentityProviderResponse:
    out: CreateIdentityProviderResponse = {}  # type: ignore[typeddict-item]
    if "identityProviderArn" in data:
        out["identity_provider_arn"] = data["identityProviderArn"]
    else:
        raise DeserializationError(
            "CreateIdentityProviderResponse.identity_provider_arn required"
        )
    return out
