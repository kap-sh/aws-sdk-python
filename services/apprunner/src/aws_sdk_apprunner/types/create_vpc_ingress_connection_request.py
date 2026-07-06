"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateVpcIngressConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.ingress_vpc_configuration
    import aws_sdk_apprunner.types.tag_list
    import aws_sdk_apprunner.types.vpc_ingress_connection_name


class CreateVpcIngressConnectionRequest(TypedDict, closed=True):
    service_arn: "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) for this App Runner service that is used to create the VPC Ingress Connection resource.</p>"""
    vpc_ingress_connection_name: (
        "aws_sdk_apprunner.types.vpc_ingress_connection_name.VpcIngressConnectionName"
    )
    """<p>A name for the VPC Ingress Connection resource. It must be unique across all the active VPC Ingress Connections in your Amazon Web Services account in the Amazon Web Services Region. </p>"""
    ingress_vpc_configuration: (
        "aws_sdk_apprunner.types.ingress_vpc_configuration.IngressVpcConfiguration"
    )
    """<p>Specifications for the customer’s Amazon VPC and the related Amazon Web Services PrivateLink VPC endpoint that are used to create the VPC Ingress Connection resource.</p>"""
    tags: NotRequired["aws_sdk_apprunner.types.tag_list.TagList"]
    """<p>An optional list of metadata items that you can associate with the VPC Ingress Connection resource. A tag is a key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVpcIngressConnectionRequest) -> dict:
    out: dict = {}
    out["ServiceArn"] = value["service_arn"]
    out["VpcIngressConnectionName"] = value["vpc_ingress_connection_name"]
    import aws_sdk_apprunner.types.ingress_vpc_configuration

    out["IngressVpcConfiguration"] = (
        aws_sdk_apprunner.types.ingress_vpc_configuration.serialize_aws_json_1_0(
            value["ingress_vpc_configuration"]
        )
    )
    if "tags" in value:
        import aws_sdk_apprunner.types.tag_list

        out["Tags"] = aws_sdk_apprunner.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVpcIngressConnectionRequest:
    out: CreateVpcIngressConnectionRequest = {}  # type: ignore[typeddict-item]
    if "ServiceArn" in data:
        out["service_arn"] = data["ServiceArn"]
    else:
        raise DeserializationError(
            "CreateVpcIngressConnectionRequest.service_arn required"
        )
    if "VpcIngressConnectionName" in data:
        out["vpc_ingress_connection_name"] = data["VpcIngressConnectionName"]
    else:
        raise DeserializationError(
            "CreateVpcIngressConnectionRequest.vpc_ingress_connection_name required"
        )
    if "IngressVpcConfiguration" in data:
        import aws_sdk_apprunner.types.ingress_vpc_configuration

        out["ingress_vpc_configuration"] = (
            aws_sdk_apprunner.types.ingress_vpc_configuration.deserialize_aws_json_1_0(
                data["IngressVpcConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateVpcIngressConnectionRequest.ingress_vpc_configuration required"
        )
    if "Tags" in data:
        import aws_sdk_apprunner.types.tag_list

        out["tags"] = aws_sdk_apprunner.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
