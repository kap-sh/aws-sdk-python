"""Generated from Smithy shape ``com.amazonaws.apprunner#DeleteVpcIngressConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.vpc_ingress_connection


class DeleteVpcIngressConnectionResponse(TypedDict, closed=True):
    vpc_ingress_connection: (
        "aws_sdk_apprunner.types.vpc_ingress_connection.VpcIngressConnection"
    )
    """<p>A description of the App Runner VPC Ingress Connection that this request just deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVpcIngressConnectionResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.vpc_ingress_connection

    out["VpcIngressConnection"] = (
        aws_sdk_apprunner.types.vpc_ingress_connection.serialize_aws_json_1_0(
            value["vpc_ingress_connection"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVpcIngressConnectionResponse:
    out: DeleteVpcIngressConnectionResponse = {}  # type: ignore[typeddict-item]
    if "VpcIngressConnection" in data:
        import aws_sdk_apprunner.types.vpc_ingress_connection

        out["vpc_ingress_connection"] = (
            aws_sdk_apprunner.types.vpc_ingress_connection.deserialize_aws_json_1_0(
                data["VpcIngressConnection"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteVpcIngressConnectionResponse.vpc_ingress_connection required"
        )
    return out
