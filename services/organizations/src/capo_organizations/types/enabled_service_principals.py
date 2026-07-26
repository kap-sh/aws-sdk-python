"""Generated from Smithy shape ``com.amazonaws.organizations#EnabledServicePrincipals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.enabled_service_principal

EnabledServicePrincipals: TypeAlias = list[
    "capo_organizations.types.enabled_service_principal.EnabledServicePrincipal"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnabledServicePrincipals) -> list:
    import capo_organizations.types.enabled_service_principal

    out: list = []
    for item in value:
        out.append(
            capo_organizations.types.enabled_service_principal.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EnabledServicePrincipals:
    import capo_organizations.types.enabled_service_principal

    out: EnabledServicePrincipals = []
    for item in data:
        out.append(
            capo_organizations.types.enabled_service_principal.deserialize_aws_json_1_1(
                item
            )
        )
    return out
