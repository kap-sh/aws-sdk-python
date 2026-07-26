"""Generated from Smithy shape ``com.amazonaws.redshift#PartnerIntegrationOutputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.partner_integration_database_name
    import capo_redshift.types.partner_integration_partner_name


class PartnerIntegrationOutputMessage(TypedDict, closed=True):
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
    value: PartnerIntegrationOutputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "database_name" in value:
        pairs.append((f"{prefix}.DatabaseName", str(value["database_name"])))
    if "partner_name" in value:
        pairs.append((f"{prefix}.PartnerName", str(value["partner_name"])))


def deserialize_query(el: Element) -> PartnerIntegrationOutputMessage:
    out: PartnerIntegrationOutputMessage = {}  # type: ignore[typeddict-item]
    child_database_name = el.find("DatabaseName")
    if child_database_name is not None:
        out["database_name"] = str(child_database_name.text or "")
    child_partner_name = el.find("PartnerName")
    if child_partner_name is not None:
        out["partner_name"] = str(child_partner_name.text or "")
    return out
