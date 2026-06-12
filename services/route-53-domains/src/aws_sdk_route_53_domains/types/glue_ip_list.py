"""Generated from Smithy shape ``com.amazonaws.route53domains#GlueIpList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.glue_ip

GlueIpList: TypeAlias = list["aws_sdk_route_53_domains.types.glue_ip.GlueIp"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueIpList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GlueIpList:
    return list(data)
