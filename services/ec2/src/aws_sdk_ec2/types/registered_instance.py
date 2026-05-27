"""Generated from Smithy shape ``com.amazonaws.ec2#RegisteredInstance``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ha_status
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.sql_server_license_usage
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class RegisteredInstance(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the SQL Server High Availability instance.</p>"""
    sql_server_license_usage: NotRequired[
        "aws_sdk_ec2.types.sql_server_license_usage.SqlServerLicenseUsage"
    ]
    """<p>The license type for the SQL Server license. Valid values include:</p> <ul> <li> <p> <code>full</code> - The SQL Server High Availability instance is using a full SQL Server license.</p> </li> <li> <p> <code>waived</code> - The SQL Server High Availability instance is waived from the SQL Server license.</p> </li> </ul>"""
    ha_status: NotRequired["aws_sdk_ec2.types.ha_status.HaStatus"]
    """<p>The SQL Server High Availability status of the instance. Valid values are:</p> <ul> <li> <p> <code>processing</code> - The SQL Server High Availability status for the SQL Server High Availability instance is being updated.</p> </li> <li> <p> <code>active</code> - The SQL Server High Availability instance is an active node in an SQL Server High Availability cluster.</p> </li> <li> <p> <code>standby</code> - The SQL Server High Availability instance is a standby failover node in an SQL Server High Availability cluster.</p> </li> <li> <p> <code>invalid</code> - An error occurred due to misconfigured permissions, or unable to dertemine SQL Server High Availability status for the SQL Server High Availability instance.</p> </li> </ul>"""
    processing_status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief description of the SQL Server High Availability status. If the instance is in the <code>invalid</code> High Availability status, this parameter includes the error message.</p>"""
    last_updated_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the instance's SQL Server High Availability status was last updated, in the ISO 8601 format in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""
    sql_server_credentials: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the Secrets Manager secret containing the SQL Server access credentials for the SQL Server High Availability instance. If not specified, deafult local user credentials will be used by the Amazon Web Services Systems Manager agent.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the SQL Server High Availability instance.</p>"""
