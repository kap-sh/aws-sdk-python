"""Generated from Smithy shape ``com.amazonaws.redshift#PartnerIntegrationInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.partner_integration_database_name
    import aws_sdk_redshift.types.partner_integration_partner_name
    import aws_sdk_redshift.types.partner_integration_status
    import aws_sdk_redshift.types.partner_integration_status_message
    import aws_sdk_redshift.types.t_stamp


class PartnerIntegrationInfo(TypedDict):
    database_name: NotRequired[
        "aws_sdk_redshift.types.partner_integration_database_name.PartnerIntegrationDatabaseName"
    ]
    """<p>The name of the database that receives data from a partner.</p>"""
    partner_name: NotRequired[
        "aws_sdk_redshift.types.partner_integration_partner_name.PartnerIntegrationPartnerName"
    ]
    """<p>The name of the partner.</p>"""
    status: NotRequired[
        "aws_sdk_redshift.types.partner_integration_status.PartnerIntegrationStatus"
    ]
    """<p>The partner integration status.</p>"""
    status_message: NotRequired[
        "aws_sdk_redshift.types.partner_integration_status_message.PartnerIntegrationStatusMessage"
    ]
    """<p>The status message provided by the partner.</p>"""
    created_at: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>The date (UTC) that the partner integration was created.</p>"""
    updated_at: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>The date (UTC) that the partner integration status was last updated by the partner.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PartnerIntegrationInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "database_name" in value:
        pairs.append((f"{prefix}.DatabaseName", str(value["database_name"])))
    if "partner_name" in value:
        pairs.append((f"{prefix}.PartnerName", str(value["partner_name"])))
    if "status" in value:
        import aws_sdk_redshift.types.partner_integration_status

        aws_sdk_redshift.types.partner_integration_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "created_at" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["created_at"], pairs, f"{prefix}.CreatedAt"
        )
    if "updated_at" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["updated_at"], pairs, f"{prefix}.UpdatedAt"
        )


def deserialize_query(el: Element) -> PartnerIntegrationInfo:
    out: PartnerIntegrationInfo = {}  # type: ignore[typeddict-item]
    child_database_name = el.find("DatabaseName")
    if child_database_name is not None:
        out["database_name"] = str(child_database_name.text or "")
    child_partner_name = el.find("PartnerName")
    if child_partner_name is not None:
        out["partner_name"] = str(child_partner_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_redshift.types.partner_integration_status

        out["status"] = (
            aws_sdk_redshift.types.partner_integration_status.deserialize_query(
                child_status
            )
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_created_at = el.find("CreatedAt")
    if child_created_at is not None:
        import aws_sdk_redshift.types.t_stamp

        out["created_at"] = aws_sdk_redshift.types.t_stamp.deserialize_query(
            child_created_at
        )
    child_updated_at = el.find("UpdatedAt")
    if child_updated_at is not None:
        import aws_sdk_redshift.types.t_stamp

        out["updated_at"] = aws_sdk_redshift.types.t_stamp.deserialize_query(
            child_updated_at
        )
    return out
