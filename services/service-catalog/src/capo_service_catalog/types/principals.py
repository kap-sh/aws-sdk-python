"""Generated from Smithy shape ``com.amazonaws.servicecatalog#Principals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.principal

Principals: TypeAlias = list["capo_service_catalog.types.principal.Principal"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Principals) -> list:
    import capo_service_catalog.types.principal

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.principal.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Principals:
    import capo_service_catalog.types.principal

    out: Principals = []
    for item in data:
        out.append(capo_service_catalog.types.principal.deserialize_aws_json_1_1(item))
    return out
