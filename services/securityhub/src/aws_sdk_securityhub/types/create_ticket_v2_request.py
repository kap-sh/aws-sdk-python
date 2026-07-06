"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateTicketV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.client_token
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.ticket_creation_mode


class CreateTicketV2Request(TypedDict, closed=True):
    connector_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The UUID of the connectorV2 to identify connectorV2 resource.</p>"""
    finding_metadata_uid: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The the unique ID for the finding.</p>"""
    client_token: NotRequired["aws_sdk_securityhub.types.client_token.ClientToken"]
    """<p>The client idempotency token.</p>"""
    mode: NotRequired[
        "aws_sdk_securityhub.types.ticket_creation_mode.TicketCreationMode"
    ]
    """<p>The mode for ticket creation. When set to DRYRUN, the ticket is created using a Security Hub owned template test finding to verify the integration is working correctly.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTicketV2Request) -> dict:
    out: dict = {}
    if "connector_id" in value:
        out["ConnectorId"] = value["connector_id"]
    if "finding_metadata_uid" in value:
        out["FindingMetadataUid"] = value["finding_metadata_uid"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "mode" in value:
        import aws_sdk_securityhub.types.ticket_creation_mode

        out["Mode"] = aws_sdk_securityhub.types.ticket_creation_mode.serialize_json(
            value["mode"]
        )
    return out


def deserialize_json(data: dict) -> CreateTicketV2Request:
    out: CreateTicketV2Request = {}  # type: ignore[typeddict-item]
    if "ConnectorId" in data:
        out["connector_id"] = data["ConnectorId"]
    if "FindingMetadataUid" in data:
        out["finding_metadata_uid"] = data["FindingMetadataUid"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Mode" in data:
        import aws_sdk_securityhub.types.ticket_creation_mode

        out["mode"] = aws_sdk_securityhub.types.ticket_creation_mode.deserialize_json(
            data["Mode"]
        )
    return out
