"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateIpAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.update_ip_address

UpdateIpAddresses: TypeAlias = list[
    "aws_sdk_route53resolver.types.update_ip_address.UpdateIpAddress"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIpAddresses) -> list:
    import aws_sdk_route53resolver.types.update_ip_address

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53resolver.types.update_ip_address.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UpdateIpAddresses:
    import aws_sdk_route53resolver.types.update_ip_address

    out: UpdateIpAddresses = []
    for item in data:
        out.append(
            aws_sdk_route53resolver.types.update_ip_address.deserialize_aws_json_1_1(
                item
            )
        )
    return out
