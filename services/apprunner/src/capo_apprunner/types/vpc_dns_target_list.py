"""Generated from Smithy shape ``com.amazonaws.apprunner#VpcDNSTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apprunner.types.vpc_dns_target

VpcDNSTargetList: TypeAlias = list["capo_apprunner.types.vpc_dns_target.VpcDNSTarget"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcDNSTargetList) -> list:
    import capo_apprunner.types.vpc_dns_target

    out: list = []
    for item in value:
        out.append(capo_apprunner.types.vpc_dns_target.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> VpcDNSTargetList:
    import capo_apprunner.types.vpc_dns_target

    out: VpcDNSTargetList = []
    for item in data:
        out.append(capo_apprunner.types.vpc_dns_target.deserialize_aws_json_1_0(item))
    return out
