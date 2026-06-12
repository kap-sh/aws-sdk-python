"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateGroupCertificateAuthorityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class CreateGroupCertificateAuthorityRequest(TypedDict):
    amzn_client_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    group_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupCertificateAuthorityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateGroupCertificateAuthorityRequest:
    out: CreateGroupCertificateAuthorityRequest = {}  # type: ignore[typeddict-item]
    return out
