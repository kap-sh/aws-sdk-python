"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateVpcConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.string_list
    import aws_sdk_apprunner.types.tag_list
    import aws_sdk_apprunner.types.vpc_connector_name


class CreateVpcConnectorRequest(TypedDict):
    vpc_connector_name: "aws_sdk_apprunner.types.vpc_connector_name.VpcConnectorName"
    """<p>A name for the VPC connector.</p>"""
    subnets: "aws_sdk_apprunner.types.string_list.StringList"
    """<p>A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.</p> <note> <p> App Runner only supports subnets of IP address type <i>IPv4</i> and <i>dual stack</i> (IPv4 and IPv6).</p> </note>"""
    security_groups: NotRequired["aws_sdk_apprunner.types.string_list.StringList"]
    """<p>A list of IDs of security groups that App Runner should use for access to Amazon Web Services resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.</p>"""
    tags: NotRequired["aws_sdk_apprunner.types.tag_list.TagList"]
    """<p>A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVpcConnectorRequest) -> dict:
    out: dict = {}
    out["VpcConnectorName"] = value["vpc_connector_name"]
    import aws_sdk_apprunner.types.string_list

    out["Subnets"] = aws_sdk_apprunner.types.string_list.serialize_aws_json_1_0(
        value["subnets"]
    )
    if "security_groups" in value:
        import aws_sdk_apprunner.types.string_list

        out["SecurityGroups"] = (
            aws_sdk_apprunner.types.string_list.serialize_aws_json_1_0(
                value["security_groups"]
            )
        )
    if "tags" in value:
        import aws_sdk_apprunner.types.tag_list

        out["Tags"] = aws_sdk_apprunner.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVpcConnectorRequest:
    out: CreateVpcConnectorRequest = {}  # type: ignore[typeddict-item]
    if "VpcConnectorName" in data:
        out["vpc_connector_name"] = data["VpcConnectorName"]
    else:
        raise DeserializationError(
            "CreateVpcConnectorRequest.vpc_connector_name required"
        )
    if "Subnets" in data:
        import aws_sdk_apprunner.types.string_list

        out["subnets"] = aws_sdk_apprunner.types.string_list.deserialize_aws_json_1_0(
            data["Subnets"]
        )
    else:
        raise DeserializationError("CreateVpcConnectorRequest.subnets required")
    if "SecurityGroups" in data:
        import aws_sdk_apprunner.types.string_list

        out["security_groups"] = (
            aws_sdk_apprunner.types.string_list.deserialize_aws_json_1_0(
                data["SecurityGroups"]
            )
        )
    if "Tags" in data:
        import aws_sdk_apprunner.types.tag_list

        out["tags"] = aws_sdk_apprunner.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
