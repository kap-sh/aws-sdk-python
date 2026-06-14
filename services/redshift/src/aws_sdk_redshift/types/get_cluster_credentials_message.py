"""Generated from Smithy shape ``com.amazonaws.redshift#GetClusterCredentialsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean_optional
    import aws_sdk_redshift.types.db_group_list
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string


class GetClusterCredentialsMessage(TypedDict):
    db_user: NotRequired["aws_sdk_redshift.types.string.String"]
    r"""<p>The name of a database user. If a user name matching <code>DbUser</code> exists in the database, the temporary user credentials have the same permissions as the existing user. If <code>DbUser</code> doesn't exist in the database and <code>Autocreate</code> is <code>True</code>, a new user is created using the value for <code>DbUser</code> with PUBLIC permissions. If a database user matching the value for <code>DbUser</code> doesn't exist and <code>Autocreate</code> is <code>False</code>, then the command succeeds but the connection attempt will fail because the user doesn't exist in the database.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html\">CREATE USER</a> in the Amazon Redshift Database Developer Guide. </p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 64 alphanumeric characters or hyphens. The user name can't be <code>PUBLIC</code>.</p> </li> <li> <p>Must contain uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Must not contain a colon ( : ) or slash ( / ). </p> </li> <li> <p>Cannot be a reserved word. A list of reserved words can be found in <a href=\"http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html\">Reserved Words</a> in the Amazon Redshift Database Developer Guide.</p> </li> </ul>"""
    db_name: NotRequired["aws_sdk_redshift.types.string.String"]
    r"""<p>The name of a database that <code>DbUser</code> is authorized to log on to. If <code>DbName</code> is not specified, <code>DbUser</code> can log on to any existing database.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 64 alphanumeric characters or hyphens</p> </li> <li> <p>Must contain uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Must not contain a colon ( : ) or slash ( / ). </p> </li> <li> <p>Cannot be a reserved word. A list of reserved words can be found in <a href=\"http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html\">Reserved Words</a> in the Amazon Redshift Database Developer Guide.</p> </li> </ul>"""
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The unique identifier of the cluster that contains the database for which you are requesting credentials. This parameter is case sensitive.</p>"""
    duration_seconds: NotRequired[
        "aws_sdk_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of seconds until the returned temporary password expires.</p> <p>Constraint: minimum 900, maximum 3600.</p> <p>Default: 900</p>"""
    auto_create: NotRequired["aws_sdk_redshift.types.boolean_optional.BooleanOptional"]
    """<p>Create a database user with the name specified for the user named in <code>DbUser</code> if one does not exist.</p>"""
    db_groups: NotRequired["aws_sdk_redshift.types.db_group_list.DbGroupList"]
    r"""<p>A list of the names of existing database groups that the user named in <code>DbUser</code> will join for the current session, in addition to any group memberships for an existing user. If not specified, a new user is added only to PUBLIC.</p> <p>Database group name constraints</p> <ul> <li> <p>Must be 1 to 64 alphanumeric characters or hyphens</p> </li> <li> <p>Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Must not contain a colon ( : ) or slash ( / ). </p> </li> <li> <p>Cannot be a reserved word. A list of reserved words can be found in <a href=\"http://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html\">Reserved Words</a> in the Amazon Redshift Database Developer Guide.</p> </li> </ul>"""
    custom_domain_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The custom domain name for the cluster credentials.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetClusterCredentialsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_user" in value:
        pairs.append((f"{prefix}.DbUser", str(value["db_user"])))
    if "db_name" in value:
        pairs.append((f"{prefix}.DbName", str(value["db_name"])))
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "duration_seconds" in value:
        pairs.append((f"{prefix}.DurationSeconds", str(value["duration_seconds"])))
    if "auto_create" in value:
        pairs.append(
            (f"{prefix}.AutoCreate", "true" if value["auto_create"] else "false")
        )
    if "db_groups" in value:
        import aws_sdk_redshift.types.db_group_list

        aws_sdk_redshift.types.db_group_list.serialize_query(
            value["db_groups"], pairs, f"{prefix}.DbGroups"
        )
    if "custom_domain_name" in value:
        pairs.append((f"{prefix}.CustomDomainName", str(value["custom_domain_name"])))


def deserialize_query(el: Element) -> GetClusterCredentialsMessage:
    out: GetClusterCredentialsMessage = {}  # type: ignore[typeddict-item]
    child_db_user = el.find("DbUser")
    if child_db_user is not None:
        out["db_user"] = str(child_db_user.text or "")
    child_db_name = el.find("DbName")
    if child_db_name is not None:
        out["db_name"] = str(child_db_name.text or "")
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_duration_seconds = el.find("DurationSeconds")
    if child_duration_seconds is not None:
        out["duration_seconds"] = int(child_duration_seconds.text or "")
    child_auto_create = el.find("AutoCreate")
    if child_auto_create is not None:
        out["auto_create"] = (child_auto_create.text or "").lower() == "true"
    child_db_groups = el.find("DbGroups")
    if child_db_groups is not None:
        import aws_sdk_redshift.types.db_group_list

        out["db_groups"] = aws_sdk_redshift.types.db_group_list.deserialize_query(
            child_db_groups
        )
    child_custom_domain_name = el.find("CustomDomainName")
    if child_custom_domain_name is not None:
        out["custom_domain_name"] = str(child_custom_domain_name.text or "")
    return out
