"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServicePublicDomains``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_public_domains_list
    import aws_sdk_lightsail.types.string

ContainerServicePublicDomains: TypeAlias = dict[
    "aws_sdk_lightsail.types.string.string",
    "aws_sdk_lightsail.types.container_service_public_domains_list.ContainerServicePublicDomainsList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ContainerServicePublicDomains) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_lightsail.types.container_service_public_domains_list

        out[key] = (
            aws_sdk_lightsail.types.container_service_public_domains_list.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServicePublicDomains:
    out: ContainerServicePublicDomains = {}
    for key, value in data.items():
        import aws_sdk_lightsail.types.container_service_public_domains_list

        out[key] = (
            aws_sdk_lightsail.types.container_service_public_domains_list.deserialize_aws_json_1_1(
                value
            )
        )
    return out
