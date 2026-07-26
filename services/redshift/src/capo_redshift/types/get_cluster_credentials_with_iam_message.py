"""Generated from Smithy shape ``com.amazonaws.redshift#GetClusterCredentialsWithIAMMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string


class GetClusterCredentialsWithIAMMessage(TypedDict, closed=True):
    db_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the database for which you are requesting credentials. If the database name is specified, the IAM policy must allow access to the resource <code>dbname</code> for the specified database name. If the database name is not specified, access to all databases is allowed.</p>"""
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the cluster that contains the database for which you are requesting credentials. </p>"""
    duration_seconds: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of seconds until the returned temporary password expires.</p> <p>Range: 900-3600. Default: 900.</p>"""
    custom_domain_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The custom domain name for the IAM message cluster credentials.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetClusterCredentialsWithIAMMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_name" in value:
        pairs.append((f"{prefix}.DbName", str(value["db_name"])))
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "duration_seconds" in value:
        pairs.append((f"{prefix}.DurationSeconds", str(value["duration_seconds"])))
    if "custom_domain_name" in value:
        pairs.append((f"{prefix}.CustomDomainName", str(value["custom_domain_name"])))


def deserialize_query(el: Element) -> GetClusterCredentialsWithIAMMessage:
    out: GetClusterCredentialsWithIAMMessage = {}  # type: ignore[typeddict-item]
    child_db_name = el.find("DbName")
    if child_db_name is not None:
        out["db_name"] = str(child_db_name.text or "")
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_duration_seconds = el.find("DurationSeconds")
    if child_duration_seconds is not None:
        out["duration_seconds"] = int(child_duration_seconds.text or "")
    child_custom_domain_name = el.find("CustomDomainName")
    if child_custom_domain_name is not None:
        out["custom_domain_name"] = str(child_custom_domain_name.text or "")
    return out
