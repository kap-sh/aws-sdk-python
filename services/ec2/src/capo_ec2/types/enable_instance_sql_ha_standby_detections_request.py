"""Generated from Smithy shape ``com.amazonaws.ec2#EnableInstanceSqlHaStandbyDetectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_id_update_string_list
    import capo_ec2.types.secret_arn


class EnableInstanceSqlHaStandbyDetectionsRequest(TypedDict, closed=True):
    instance_ids: NotRequired[
        "capo_ec2.types.instance_id_update_string_list.InstanceIdUpdateStringList"
    ]
    """<p>The IDs of the instances to enable for SQL Server High Availability standby detection monitoring.</p>"""
    sql_server_credentials: NotRequired["capo_ec2.types.secret_arn.SecretArn"]
    """<p>The ARN of the Secrets Manager secret containing the SQL Server access credentials. The specified secret must contain valid SQL Server credentials for the specified instances. If not specified, deafult local user credentials will be used by the Amazon Web Services Systems Manager agent. To enable instances with different credentials, you must make separate requests.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableInstanceSqlHaStandbyDetectionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_ids" in value:
        import capo_ec2.types.instance_id_update_string_list

        capo_ec2.types.instance_id_update_string_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{prefix}.InstanceIds"
        )
    if "sql_server_credentials" in value:
        pairs.append(
            (f"{prefix}.SqlServerCredentials", str(value["sql_server_credentials"]))
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> EnableInstanceSqlHaStandbyDetectionsRequest:
    out: EnableInstanceSqlHaStandbyDetectionsRequest = {}  # type: ignore[typeddict-item]
    if el.find("InstanceIds") is not None:
        import capo_ec2.types.instance_id_update_string_list

        out["instance_ids"] = (
            capo_ec2.types.instance_id_update_string_list.deserialize_ec2_query(
                el, "InstanceIds"
            )
        )
    child_sql_server_credentials = el.find("SqlServerCredentials")
    if child_sql_server_credentials is not None:
        out["sql_server_credentials"] = str(child_sql_server_credentials.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
