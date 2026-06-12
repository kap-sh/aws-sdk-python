"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServiceServiceRegistriesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_service_service_registries_details

AwsEcsServiceServiceRegistriesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_service_service_registries_details.AwsEcsServiceServiceRegistriesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServiceServiceRegistriesList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_service_service_registries_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_service_service_registries_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsServiceServiceRegistriesList:
    import aws_sdk_securityhub.types.aws_ecs_service_service_registries_details

    out: AwsEcsServiceServiceRegistriesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_service_service_registries_details.deserialize_json(
                item
            )
        )
    return out
