"""Generated from Smithy shape ``com.amazonaws.codestarconnections#GetHostOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.host_name
    import aws_sdk_codestar_connections.types.host_status
    import aws_sdk_codestar_connections.types.provider_type
    import aws_sdk_codestar_connections.types.url
    import aws_sdk_codestar_connections.types.vpc_configuration


class GetHostOutput(TypedDict):
    name: NotRequired["aws_sdk_codestar_connections.types.host_name.HostName"]
    """<p>The name of the requested host.</p>"""
    status: NotRequired["aws_sdk_codestar_connections.types.host_status.HostStatus"]
    """<p>The status of the requested host.</p>"""
    provider_type: NotRequired[
        "aws_sdk_codestar_connections.types.provider_type.ProviderType"
    ]
    """<p>The provider type of the requested host, such as GitHub Enterprise Server.</p>"""
    provider_endpoint: NotRequired["aws_sdk_codestar_connections.types.url.Url"]
    """<p>The endpoint of the infrastructure represented by the requested host.</p>"""
    vpc_configuration: NotRequired[
        "aws_sdk_codestar_connections.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>The VPC configuration of the requested host.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetHostOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "provider_type" in value:
        import aws_sdk_codestar_connections.types.provider_type

        out["ProviderType"] = (
            aws_sdk_codestar_connections.types.provider_type.serialize_aws_json_1_0(
                value["provider_type"]
            )
        )
    if "provider_endpoint" in value:
        out["ProviderEndpoint"] = value["provider_endpoint"]
    if "vpc_configuration" in value:
        import aws_sdk_codestar_connections.types.vpc_configuration

        out["VpcConfiguration"] = (
            aws_sdk_codestar_connections.types.vpc_configuration.serialize_aws_json_1_0(
                value["vpc_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetHostOutput:
    out: GetHostOutput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "ProviderType" in data:
        import aws_sdk_codestar_connections.types.provider_type

        out["provider_type"] = (
            aws_sdk_codestar_connections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    if "ProviderEndpoint" in data:
        out["provider_endpoint"] = data["ProviderEndpoint"]
    if "VpcConfiguration" in data:
        import aws_sdk_codestar_connections.types.vpc_configuration

        out["vpc_configuration"] = (
            aws_sdk_codestar_connections.types.vpc_configuration.deserialize_aws_json_1_0(
                data["VpcConfiguration"]
            )
        )
    return out
