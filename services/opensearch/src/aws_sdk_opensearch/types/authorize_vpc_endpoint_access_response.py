"""Generated from Smithy shape ``com.amazonaws.opensearch#AuthorizeVpcEndpointAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.authorized_principal


class AuthorizeVpcEndpointAccessResponse(TypedDict, closed=True):
    authorized_principal: (
        "aws_sdk_opensearch.types.authorized_principal.AuthorizedPrincipal"
    )
    """<p>Information about the Amazon Web Services account or service that was provided access to the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizeVpcEndpointAccessResponse) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.authorized_principal

    out["AuthorizedPrincipal"] = (
        aws_sdk_opensearch.types.authorized_principal.serialize_json(
            value["authorized_principal"]
        )
    )
    return out


def deserialize_json(data: dict) -> AuthorizeVpcEndpointAccessResponse:
    out: AuthorizeVpcEndpointAccessResponse = {}  # type: ignore[typeddict-item]
    if "AuthorizedPrincipal" in data:
        import aws_sdk_opensearch.types.authorized_principal

        out["authorized_principal"] = (
            aws_sdk_opensearch.types.authorized_principal.deserialize_json(
                data["AuthorizedPrincipal"]
            )
        )
    else:
        raise DeserializationError(
            "AuthorizeVpcEndpointAccessResponse.authorized_principal required"
        )
    return out
