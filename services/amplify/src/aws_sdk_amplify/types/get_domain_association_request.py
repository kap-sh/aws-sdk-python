"""Generated from Smithy shape ``com.amazonaws.amplify#GetDomainAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.domain_name


class GetDomainAssociationRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplify.types.app_id.AppId"
    """<p> The unique id for an Amplify app. </p>"""
    domain_name: "aws_sdk_amplify.types.domain_name.DomainName"
    """<p> The name of the domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainAssociationRequest:
    out: GetDomainAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
