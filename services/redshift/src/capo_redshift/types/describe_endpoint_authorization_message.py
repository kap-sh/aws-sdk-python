"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeEndpointAuthorizationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean_optional
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string


class DescribeEndpointAuthorizationMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The cluster identifier of the cluster to access.</p>"""
    account: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Web Services account ID of either the cluster owner (grantor) or grantee. If <code>Grantee</code> parameter is true, then the <code>Account</code> value is of the grantor.</p>"""
    grantee: NotRequired["capo_redshift.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether to check authorization from a grantor or grantee point of view. If true, Amazon Redshift returns endpoint authorizations that you've been granted. If false (default), checks authorization from a grantor point of view.</p>"""
    max_records: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a <code>Marker</code> is included in the response so that the remaining results can be retrieved.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeEndpointAuthorization</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the <code>MaxRecords</code> parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEndpointAuthorizationMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "account" in value:
        pairs.append((f"{prefix}.Account", str(value["account"])))
    if "grantee" in value:
        pairs.append((f"{prefix}.Grantee", "true" if value["grantee"] else "false"))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeEndpointAuthorizationMessage:
    out: DescribeEndpointAuthorizationMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_account = el.find("Account")
    if child_account is not None:
        out["account"] = str(child_account.text or "")
    child_grantee = el.find("Grantee")
    if child_grantee is not None:
        out["grantee"] = (child_grantee.text or "").lower() == "true"
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
