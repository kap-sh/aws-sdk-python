"""Generated from Smithy shape ``com.amazonaws.redshift#UpdatePartnerStatusInputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.partner_integration_account_id
    import capo_redshift.types.partner_integration_cluster_identifier
    import capo_redshift.types.partner_integration_database_name
    import capo_redshift.types.partner_integration_partner_name
    import capo_redshift.types.partner_integration_status
    import capo_redshift.types.partner_integration_status_message


class UpdatePartnerStatusInputMessage(TypedDict, closed=True):
    account_id: NotRequired[
        "capo_redshift.types.partner_integration_account_id.PartnerIntegrationAccountId"
    ]
    """<p>The Amazon Web Services account ID that owns the cluster.</p>"""
    cluster_identifier: NotRequired[
        "capo_redshift.types.partner_integration_cluster_identifier.PartnerIntegrationClusterIdentifier"
    ]
    """<p>The cluster identifier of the cluster whose partner integration status is being updated.</p>"""
    database_name: NotRequired[
        "capo_redshift.types.partner_integration_database_name.PartnerIntegrationDatabaseName"
    ]
    """<p>The name of the database whose partner integration status is being updated.</p>"""
    partner_name: NotRequired[
        "capo_redshift.types.partner_integration_partner_name.PartnerIntegrationPartnerName"
    ]
    """<p>The name of the partner whose integration status is being updated.</p>"""
    status: NotRequired[
        "capo_redshift.types.partner_integration_status.PartnerIntegrationStatus"
    ]
    """<p>The value of the updated status.</p>"""
    status_message: NotRequired[
        "capo_redshift.types.partner_integration_status_message.PartnerIntegrationStatusMessage"
    ]
    """<p>The status message provided by the partner.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdatePartnerStatusInputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "account_id" in value:
        pairs.append((f"{prefix}.AccountId", str(value["account_id"])))
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "database_name" in value:
        pairs.append((f"{prefix}.DatabaseName", str(value["database_name"])))
    if "partner_name" in value:
        pairs.append((f"{prefix}.PartnerName", str(value["partner_name"])))
    if "status" in value:
        import capo_redshift.types.partner_integration_status

        capo_redshift.types.partner_integration_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))


def deserialize_query(el: Element) -> UpdatePartnerStatusInputMessage:
    out: UpdatePartnerStatusInputMessage = {}  # type: ignore[typeddict-item]
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
    child_status = el.find("Status")
    if child_status is not None:
        import capo_redshift.types.partner_integration_status

        out["status"] = (
            capo_redshift.types.partner_integration_status.deserialize_query(
                child_status
            )
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    return out
