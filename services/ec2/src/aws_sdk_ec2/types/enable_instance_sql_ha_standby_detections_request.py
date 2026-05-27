"""Generated from Smithy shape ``com.amazonaws.ec2#EnableInstanceSqlHaStandbyDetectionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_id_update_string_list
    import aws_sdk_ec2.types.secret_arn


class EnableInstanceSqlHaStandbyDetectionsRequest(TypedDict):
    instance_ids: NotRequired[
        "aws_sdk_ec2.types.instance_id_update_string_list.InstanceIdUpdateStringList"
    ]
    """<p>The IDs of the instances to enable for SQL Server High Availability standby detection monitoring.</p>"""
    sql_server_credentials: NotRequired["aws_sdk_ec2.types.secret_arn.SecretArn"]
    """<p>The ARN of the Secrets Manager secret containing the SQL Server access credentials. The specified secret must contain valid SQL Server credentials for the specified instances. If not specified, deafult local user credentials will be used by the Amazon Web Services Systems Manager agent. To enable instances with different credentials, you must make separate requests.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
