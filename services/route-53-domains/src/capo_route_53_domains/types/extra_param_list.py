"""Generated from Smithy shape ``com.amazonaws.route53domains#ExtraParamList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route_53_domains.types.extra_param

ExtraParamList: TypeAlias = list["capo_route_53_domains.types.extra_param.ExtraParam"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtraParamList) -> list:
    import capo_route_53_domains.types.extra_param

    out: list = []
    for item in value:
        out.append(capo_route_53_domains.types.extra_param.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExtraParamList:
    import capo_route_53_domains.types.extra_param

    out: ExtraParamList = []
    for item in data:
        out.append(
            capo_route_53_domains.types.extra_param.deserialize_aws_json_1_1(item)
        )
    return out
