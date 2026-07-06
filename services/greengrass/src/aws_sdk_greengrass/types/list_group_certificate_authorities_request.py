"""Generated from Smithy shape ``com.amazonaws.greengrass#ListGroupCertificateAuthoritiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class ListGroupCertificateAuthoritiesRequest(TypedDict, closed=True):
    group_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupCertificateAuthoritiesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGroupCertificateAuthoritiesRequest:
    out: ListGroupCertificateAuthoritiesRequest = {}  # type: ignore[typeddict-item]
    return out
