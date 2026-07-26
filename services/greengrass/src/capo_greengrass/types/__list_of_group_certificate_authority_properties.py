"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfGroupCertificateAuthorityProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.group_certificate_authority_properties

__listOfGroupCertificateAuthorityProperties: TypeAlias = list[
    "capo_greengrass.types.group_certificate_authority_properties.GroupCertificateAuthorityProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfGroupCertificateAuthorityProperties) -> list:
    import capo_greengrass.types.group_certificate_authority_properties

    out: list = []
    for item in value:
        out.append(
            capo_greengrass.types.group_certificate_authority_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfGroupCertificateAuthorityProperties:
    import capo_greengrass.types.group_certificate_authority_properties

    out: __listOfGroupCertificateAuthorityProperties = []
    for item in data:
        out.append(
            capo_greengrass.types.group_certificate_authority_properties.deserialize_json(
                item
            )
        )
    return out
