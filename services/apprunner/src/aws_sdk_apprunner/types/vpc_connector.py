"""Generated from Smithy shape ``com.amazonaws.apprunner#VpcConnector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.integer
    import aws_sdk_apprunner.types.string_list
    import aws_sdk_apprunner.types.timestamp
    import aws_sdk_apprunner.types.vpc_connector_name
    import aws_sdk_apprunner.types.vpc_connector_status


class VpcConnector(TypedDict):
    vpc_connector_name: NotRequired[
        "aws_sdk_apprunner.types.vpc_connector_name.VpcConnectorName"
    ]
    """<p>The customer-provided VPC connector name.</p>"""
    vpc_connector_arn: NotRequired[
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of this VPC connector.</p>"""
    vpc_connector_revision: "aws_sdk_apprunner.types.integer.Integer"
    """<p>The revision of this VPC connector. It's unique among all the active connectors (<code>\"Status\": \"ACTIVE\"</code>) that share the same <code>Name</code>.</p> <note> <p>At this time, App Runner supports only one revision per name.</p> </note>"""
    subnets: NotRequired["aws_sdk_apprunner.types.string_list.StringList"]
    """<p>A list of IDs of subnets that App Runner uses for your service. All IDs are of subnets of a single Amazon VPC.</p>"""
    security_groups: NotRequired["aws_sdk_apprunner.types.string_list.StringList"]
    """<p>A list of IDs of security groups that App Runner uses for access to Amazon Web Services resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.</p>"""
    status: NotRequired[
        "aws_sdk_apprunner.types.vpc_connector_status.VpcConnectorStatus"
    ]
    """<p>The current state of the VPC connector. If the status of a connector revision is <code>INACTIVE</code>, it was deleted and can't be used. Inactive connector revisions are permanently removed some time after they are deleted.</p>"""
    created_at: NotRequired["aws_sdk_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the VPC connector was created. It's in Unix time stamp format.</p>"""
    deleted_at: NotRequired["aws_sdk_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the VPC connector was deleted. It's in Unix time stamp format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcConnector) -> dict:
    out: dict = {}
    if "vpc_connector_name" in value:
        out["VpcConnectorName"] = value["vpc_connector_name"]
    if "vpc_connector_arn" in value:
        out["VpcConnectorArn"] = value["vpc_connector_arn"]
    out["VpcConnectorRevision"] = value.get("vpc_connector_revision", 0)
    if "subnets" in value:
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
    if "status" in value:
        import aws_sdk_apprunner.types.vpc_connector_status

        out["Status"] = (
            aws_sdk_apprunner.types.vpc_connector_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "created_at" in value:
        import aws_sdk_apprunner.types.timestamp

        out["CreatedAt"] = aws_sdk_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "deleted_at" in value:
        import aws_sdk_apprunner.types.timestamp

        out["DeletedAt"] = aws_sdk_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["deleted_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcConnector:
    out: VpcConnector = {}  # type: ignore[typeddict-item]
    if "VpcConnectorName" in data:
        out["vpc_connector_name"] = data["VpcConnectorName"]
    if "VpcConnectorArn" in data:
        out["vpc_connector_arn"] = data["VpcConnectorArn"]
    if "VpcConnectorRevision" in data:
        out["vpc_connector_revision"] = data["VpcConnectorRevision"]
    else:
        out["vpc_connector_revision"] = 0
    if "Subnets" in data:
        import aws_sdk_apprunner.types.string_list

        out["subnets"] = aws_sdk_apprunner.types.string_list.deserialize_aws_json_1_0(
            data["Subnets"]
        )
    if "SecurityGroups" in data:
        import aws_sdk_apprunner.types.string_list

        out["security_groups"] = (
            aws_sdk_apprunner.types.string_list.deserialize_aws_json_1_0(
                data["SecurityGroups"]
            )
        )
    if "Status" in data:
        import aws_sdk_apprunner.types.vpc_connector_status

        out["status"] = (
            aws_sdk_apprunner.types.vpc_connector_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_apprunner.types.timestamp

        out["created_at"] = aws_sdk_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if "DeletedAt" in data:
        import aws_sdk_apprunner.types.timestamp

        out["deleted_at"] = aws_sdk_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["DeletedAt"]
        )
    return out
