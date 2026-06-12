"""Generated from Smithy shape ``com.amazonaws.apprunner#UpdateVpcIngressConnectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.vpc_ingress_connection


class UpdateVpcIngressConnectionResponse(TypedDict):
    vpc_ingress_connection: (
        "aws_sdk_apprunner.types.vpc_ingress_connection.VpcIngressConnection"
    )
    """<p>A description of the App Runner VPC Ingress Connection resource that's updated by this request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateVpcIngressConnectionResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.vpc_ingress_connection

    out["VpcIngressConnection"] = (
        aws_sdk_apprunner.types.vpc_ingress_connection.serialize_aws_json_1_0(
            value["vpc_ingress_connection"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateVpcIngressConnectionResponse:
    out: UpdateVpcIngressConnectionResponse = {}  # type: ignore[typeddict-item]
    if "VpcIngressConnection" in data:
        import aws_sdk_apprunner.types.vpc_ingress_connection

        out["vpc_ingress_connection"] = (
            aws_sdk_apprunner.types.vpc_ingress_connection.deserialize_aws_json_1_0(
                data["VpcIngressConnection"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateVpcIngressConnectionResponse.vpc_ingress_connection required"
        )
    return out
