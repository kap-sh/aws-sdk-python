"""Generated from Smithy shape ``com.amazonaws.redshift#EndpointAuthorization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.authorization_status
    import capo_redshift.types.boolean
    import capo_redshift.types.integer
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp
    import capo_redshift.types.vpc_identifier_list


class EndpointAuthorization(TypedDict, closed=True):
    grantor: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Web Services account ID of the cluster owner.</p>"""
    grantee: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Web Services account ID of the grantee of the cluster.</p>"""
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The cluster identifier.</p>"""
    authorize_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The time (UTC) when the authorization was created.</p>"""
    cluster_status: NotRequired["capo_redshift.types.string.String"]
    """<p>The status of the cluster.</p>"""
    status: NotRequired["capo_redshift.types.authorization_status.AuthorizationStatus"]
    """<p>The status of the authorization action.</p>"""
    allowed_all_vp_cs: NotRequired["capo_redshift.types.boolean.Boolean"]
    """<p>Indicates whether all VPCs in the grantee account are allowed access to the cluster.</p>"""
    allowed_vp_cs: NotRequired[
        "capo_redshift.types.vpc_identifier_list.VpcIdentifierList"
    ]
    """<p>The VPCs allowed access to the cluster.</p>"""
    endpoint_count: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The number of Redshift-managed VPC endpoints created for the authorization.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EndpointAuthorization, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "grantor" in value:
        pairs.append((f"{prefix}.Grantor", str(value["grantor"])))
    if "grantee" in value:
        pairs.append((f"{prefix}.Grantee", str(value["grantee"])))
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "authorize_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["authorize_time"], pairs, f"{prefix}.AuthorizeTime"
        )
    if "cluster_status" in value:
        pairs.append((f"{prefix}.ClusterStatus", str(value["cluster_status"])))
    if "status" in value:
        import capo_redshift.types.authorization_status

        capo_redshift.types.authorization_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "allowed_all_vp_cs" in value:
        pairs.append(
            (
                f"{prefix}.AllowedAllVPCs",
                "true" if value["allowed_all_vp_cs"] else "false",
            )
        )
    if "allowed_vp_cs" in value:
        import capo_redshift.types.vpc_identifier_list

        capo_redshift.types.vpc_identifier_list.serialize_query(
            value["allowed_vp_cs"], pairs, f"{prefix}.AllowedVPCs"
        )
    if "endpoint_count" in value:
        pairs.append((f"{prefix}.EndpointCount", str(value["endpoint_count"])))


def deserialize_query(el: Element) -> EndpointAuthorization:
    out: EndpointAuthorization = {}  # type: ignore[typeddict-item]
    child_grantor = el.find("Grantor")
    if child_grantor is not None:
        out["grantor"] = str(child_grantor.text or "")
    child_grantee = el.find("Grantee")
    if child_grantee is not None:
        out["grantee"] = str(child_grantee.text or "")
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_authorize_time = el.find("AuthorizeTime")
    if child_authorize_time is not None:
        import capo_redshift.types.t_stamp

        out["authorize_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_authorize_time
        )
    child_cluster_status = el.find("ClusterStatus")
    if child_cluster_status is not None:
        out["cluster_status"] = str(child_cluster_status.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_redshift.types.authorization_status

        out["status"] = capo_redshift.types.authorization_status.deserialize_query(
            child_status
        )
    child_allowed_all_vp_cs = el.find("AllowedAllVPCs")
    if child_allowed_all_vp_cs is not None:
        out["allowed_all_vp_cs"] = (
            child_allowed_all_vp_cs.text or ""
        ).lower() == "true"
    child_allowed_vp_cs = el.find("AllowedVPCs")
    if child_allowed_vp_cs is not None:
        import capo_redshift.types.vpc_identifier_list

        out["allowed_vp_cs"] = (
            capo_redshift.types.vpc_identifier_list.deserialize_query(
                child_allowed_vp_cs
            )
        )
    child_endpoint_count = el.find("EndpointCount")
    if child_endpoint_count is not None:
        out["endpoint_count"] = int(child_endpoint_count.text or "")
    return out
