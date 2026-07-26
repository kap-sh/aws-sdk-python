"""Generated from Smithy shape ``com.amazonaws.greengrass#ListGroupCertificateAuthoritiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_group_certificate_authority_properties


class ListGroupCertificateAuthoritiesResponse(TypedDict, closed=True):
    group_certificate_authorities: NotRequired[
        "capo_greengrass.types.__list_of_group_certificate_authority_properties.__listOfGroupCertificateAuthorityProperties"
    ]
    """A list of certificate authorities associated with the group."""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupCertificateAuthoritiesResponse) -> dict:
    out: dict = {}
    if "group_certificate_authorities" in value:
        import capo_greengrass.types.__list_of_group_certificate_authority_properties

        out["GroupCertificateAuthorities"] = (
            capo_greengrass.types.__list_of_group_certificate_authority_properties.serialize_json(
                value["group_certificate_authorities"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListGroupCertificateAuthoritiesResponse:
    out: ListGroupCertificateAuthoritiesResponse = {}  # type: ignore[typeddict-item]
    if "GroupCertificateAuthorities" in data:
        import capo_greengrass.types.__list_of_group_certificate_authority_properties

        out["group_certificate_authorities"] = (
            capo_greengrass.types.__list_of_group_certificate_authority_properties.deserialize_json(
                data["GroupCertificateAuthorities"]
            )
        )
    return out
