"""Generated from Smithy shape ``com.amazonaws.ec2#RegisteredInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ha_status
    import capo_ec2.types.instance_id
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.sql_server_license_usage
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class RegisteredInstance(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the SQL Server High Availability instance.</p>"""
    sql_server_license_usage: NotRequired[
        "capo_ec2.types.sql_server_license_usage.SqlServerLicenseUsage"
    ]
    """<p>The license type for the SQL Server license. Valid values include:</p> <ul> <li> <p> <code>full</code> - The SQL Server High Availability instance is using a full SQL Server license.</p> </li> <li> <p> <code>waived</code> - The SQL Server High Availability instance is waived from the SQL Server license.</p> </li> </ul>"""
    ha_status: NotRequired["capo_ec2.types.ha_status.HaStatus"]
    """<p>The SQL Server High Availability status of the instance. Valid values are:</p> <ul> <li> <p> <code>processing</code> - The SQL Server High Availability status for the SQL Server High Availability instance is being updated.</p> </li> <li> <p> <code>active</code> - The SQL Server High Availability instance is an active node in an SQL Server High Availability cluster.</p> </li> <li> <p> <code>standby</code> - The SQL Server High Availability instance is a standby failover node in an SQL Server High Availability cluster.</p> </li> <li> <p> <code>invalid</code> - An error occurred due to misconfigured permissions, or unable to dertemine SQL Server High Availability status for the SQL Server High Availability instance.</p> </li> </ul>"""
    processing_status: NotRequired["capo_ec2.types.string.String"]
    """<p>A brief description of the SQL Server High Availability status. If the instance is in the <code>invalid</code> High Availability status, this parameter includes the error message.</p>"""
    last_updated_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the instance's SQL Server High Availability status was last updated, in the ISO 8601 format in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""
    sql_server_credentials: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the Secrets Manager secret containing the SQL Server access credentials for the SQL Server High Availability instance. If not specified, deafult local user credentials will be used by the Amazon Web Services Systems Manager agent.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the SQL Server High Availability instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RegisteredInstance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "sql_server_license_usage" in value:
        import capo_ec2.types.sql_server_license_usage

        capo_ec2.types.sql_server_license_usage.serialize_ec2_query(
            value["sql_server_license_usage"],
            pairs,
            f"{key_prefix}SqlServerLicenseUsage",
        )
    if "ha_status" in value:
        import capo_ec2.types.ha_status

        capo_ec2.types.ha_status.serialize_ec2_query(
            value["ha_status"], pairs, f"{key_prefix}HaStatus"
        )
    if "processing_status" in value:
        pairs.append((f"{key_prefix}ProcessingStatus", str(value["processing_status"])))
    if "last_updated_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["last_updated_time"], pairs, f"{key_prefix}LastUpdatedTime"
        )
    if "sql_server_credentials" in value:
        pairs.append(
            (f"{key_prefix}SqlServerCredentials", str(value["sql_server_credentials"]))
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> RegisteredInstance:
    out: RegisteredInstance = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_sql_server_license_usage = el.find("sqlServerLicenseUsage")
    if child_sql_server_license_usage is not None:
        import capo_ec2.types.sql_server_license_usage

        out["sql_server_license_usage"] = (
            capo_ec2.types.sql_server_license_usage.deserialize_ec2_query(
                child_sql_server_license_usage
            )
        )
    child_ha_status = el.find("haStatus")
    if child_ha_status is not None:
        import capo_ec2.types.ha_status

        out["ha_status"] = capo_ec2.types.ha_status.deserialize_ec2_query(
            child_ha_status
        )
    child_processing_status = el.find("processingStatus")
    if child_processing_status is not None:
        out["processing_status"] = str(child_processing_status.text or "")
    child_last_updated_time = el.find("lastUpdatedTime")
    if child_last_updated_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["last_updated_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_last_updated_time
            )
        )
    child_sql_server_credentials = el.find("sqlServerCredentials")
    if child_sql_server_credentials is not None:
        out["sql_server_credentials"] = str(child_sql_server_credentials.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
