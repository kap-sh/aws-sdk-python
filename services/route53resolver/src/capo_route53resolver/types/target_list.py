"""Generated from Smithy shape ``com.amazonaws.route53resolver#TargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.target_address

TargetList: TypeAlias = list["capo_route53resolver.types.target_address.TargetAddress"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetList) -> list:
    import capo_route53resolver.types.target_address

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.target_address.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TargetList:
    import capo_route53resolver.types.target_address

    out: TargetList = []
    for item in data:
        out.append(
            capo_route53resolver.types.target_address.deserialize_aws_json_1_1(item)
        )
    return out
