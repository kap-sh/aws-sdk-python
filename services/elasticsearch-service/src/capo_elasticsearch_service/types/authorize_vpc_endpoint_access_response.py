"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AuthorizeVpcEndpointAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.authorized_principal


class AuthorizeVpcEndpointAccessResponse(TypedDict, closed=True):
    authorized_principal: (
        "capo_elasticsearch_service.types.authorized_principal.AuthorizedPrincipal"
    )
    """<p>Information about the account or service that was provided access to the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizeVpcEndpointAccessResponse) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.authorized_principal

    out["AuthorizedPrincipal"] = (
        capo_elasticsearch_service.types.authorized_principal.serialize_json(
            value["authorized_principal"]
        )
    )
    return out


def deserialize_json(data: dict) -> AuthorizeVpcEndpointAccessResponse:
    out: AuthorizeVpcEndpointAccessResponse = {}  # type: ignore[typeddict-item]
    if "AuthorizedPrincipal" in data:
        import capo_elasticsearch_service.types.authorized_principal

        out["authorized_principal"] = (
            capo_elasticsearch_service.types.authorized_principal.deserialize_json(
                data["AuthorizedPrincipal"]
            )
        )
    else:
        raise DeserializationError(
            "AuthorizeVpcEndpointAccessResponse.authorized_principal required"
        )
    return out
