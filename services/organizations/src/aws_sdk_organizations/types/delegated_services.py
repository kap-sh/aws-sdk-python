"""Generated from Smithy shape ``com.amazonaws.organizations#DelegatedServices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_organizations.types.delegated_service

DelegatedServices: TypeAlias = list[
    "aws_sdk_organizations.types.delegated_service.DelegatedService"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DelegatedServices) -> list:
    import aws_sdk_organizations.types.delegated_service

    out: list = []
    for item in value:
        out.append(
            aws_sdk_organizations.types.delegated_service.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DelegatedServices:
    import aws_sdk_organizations.types.delegated_service

    out: DelegatedServices = []
    for item in data:
        out.append(
            aws_sdk_organizations.types.delegated_service.deserialize_aws_json_1_1(item)
        )
    return out
