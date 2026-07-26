"""Generated from Smithy shape ``com.amazonaws.apprunner#DescribeVpcIngressConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.vpc_ingress_connection


class DescribeVpcIngressConnectionResponse(TypedDict, closed=True):
    vpc_ingress_connection: (
        "capo_apprunner.types.vpc_ingress_connection.VpcIngressConnection"
    )
    """<p>A description of the App Runner VPC Ingress Connection that you specified in this request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeVpcIngressConnectionResponse) -> dict:
    out: dict = {}
    import capo_apprunner.types.vpc_ingress_connection

    out["VpcIngressConnection"] = (
        capo_apprunner.types.vpc_ingress_connection.serialize_aws_json_1_0(
            value["vpc_ingress_connection"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeVpcIngressConnectionResponse:
    out: DescribeVpcIngressConnectionResponse = {}  # type: ignore[typeddict-item]
    if "VpcIngressConnection" in data:
        import capo_apprunner.types.vpc_ingress_connection

        out["vpc_ingress_connection"] = (
            capo_apprunner.types.vpc_ingress_connection.deserialize_aws_json_1_0(
                data["VpcIngressConnection"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeVpcIngressConnectionResponse.vpc_ingress_connection required"
        )
    return out
