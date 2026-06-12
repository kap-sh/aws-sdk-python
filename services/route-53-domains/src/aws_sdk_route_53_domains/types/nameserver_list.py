"""Generated from Smithy shape ``com.amazonaws.route53domains#NameserverList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.nameserver

NameserverList: TypeAlias = list["aws_sdk_route_53_domains.types.nameserver.Nameserver"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NameserverList) -> list:
    import aws_sdk_route_53_domains.types.nameserver

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route_53_domains.types.nameserver.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NameserverList:
    import aws_sdk_route_53_domains.types.nameserver

    out: NameserverList = []
    for item in data:
        out.append(
            aws_sdk_route_53_domains.types.nameserver.deserialize_aws_json_1_1(item)
        )
    return out
