"""Generated from Smithy shape ``com.amazonaws.apprunner#VpcIngressConnectionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apprunner.types.vpc_ingress_connection_summary

VpcIngressConnectionSummaryList: TypeAlias = list[
    "capo_apprunner.types.vpc_ingress_connection_summary.VpcIngressConnectionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcIngressConnectionSummaryList) -> list:
    import capo_apprunner.types.vpc_ingress_connection_summary

    out: list = []
    for item in value:
        out.append(
            capo_apprunner.types.vpc_ingress_connection_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VpcIngressConnectionSummaryList:
    import capo_apprunner.types.vpc_ingress_connection_summary

    out: VpcIngressConnectionSummaryList = []
    for item in data:
        out.append(
            capo_apprunner.types.vpc_ingress_connection_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
