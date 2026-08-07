"""Generated from Smithy shape ``com.amazonaws.redshift#PartnerIntegrationInputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.partner_integration_account_id
    import capo_redshift.types.partner_integration_cluster_identifier
    import capo_redshift.types.partner_integration_database_name
    import capo_redshift.types.partner_integration_partner_name


class PartnerIntegrationInputMessage(TypedDict, closed=True):
    account_id: NotRequired[
        "capo_redshift.types.partner_integration_account_id.PartnerIntegrationAccountId"
    ]
    """<p>The Amazon Web Services account ID that owns the cluster.</p>"""
    cluster_identifier: NotRequired[
        "capo_redshift.types.partner_integration_cluster_identifier.PartnerIntegrationClusterIdentifier"
    ]
    """<p>The cluster identifier of the cluster that receives data from the partner.</p>"""
    database_name: NotRequired[
        "capo_redshift.types.partner_integration_database_name.PartnerIntegrationDatabaseName"
    ]
    """<p>The name of the database that receives data from the partner.</p>"""
    partner_name: NotRequired[
        "capo_redshift.types.partner_integration_partner_name.PartnerIntegrationPartnerName"
    ]
    """<p>The name of the partner that is authorized to send data.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PartnerIntegrationInputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "account_id" in value:
        pairs.append((f"{key_prefix}AccountId", str(value["account_id"])))
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "database_name" in value:
        pairs.append((f"{key_prefix}DatabaseName", str(value["database_name"])))
    if "partner_name" in value:
        pairs.append((f"{key_prefix}PartnerName", str(value["partner_name"])))


def deserialize_query(el: Element) -> PartnerIntegrationInputMessage:
    out: PartnerIntegrationInputMessage = {}  # type: ignore[typeddict-item]
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_database_name = el.find("DatabaseName")
    if child_database_name is not None:
        out["database_name"] = str(child_database_name.text or "")
    child_partner_name = el.find("PartnerName")
    if child_partner_name is not None:
        out["partner_name"] = str(child_partner_name.text or "")
    return out
