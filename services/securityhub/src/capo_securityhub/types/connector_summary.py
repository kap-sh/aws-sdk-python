"""Generated from Smithy shape ``com.amazonaws.securityhub#ConnectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.provider_summary
    import capo_securityhub.types.timestamp


class ConnectorSummary(TypedDict, closed=True):
    connector_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the connectorV2.</p>"""
    connector_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The UUID of the connectorV2 to identify connectorV2 resource.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Name field contains the user-defined name assigned to the integration connector. This helps identify and manage multiple connectors within Security Hub.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The description of the connectorV2.</p>"""
    provider_summary: NotRequired[
        "capo_securityhub.types.provider_summary.ProviderSummary"
    ]
    """<p>The connectorV2 third party provider configuration summary.</p>"""
    created_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>ISO 8601 UTC timestamp for the time create the connectorV2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorSummary) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "connector_id" in value:
        out["ConnectorId"] = value["connector_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "provider_summary" in value:
        import capo_securityhub.types.provider_summary

        out["ProviderSummary"] = capo_securityhub.types.provider_summary.serialize_json(
            value["provider_summary"]
        )
    if "created_at" in value:
        import capo_securityhub.types.timestamp

        out["CreatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> ConnectorSummary:
    out: ConnectorSummary = {}  # type: ignore[typeddict-item]
    if "ConnectorArn" in data:
        out["connector_arn"] = data["ConnectorArn"]
    if "ConnectorId" in data:
        out["connector_id"] = data["ConnectorId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ProviderSummary" in data:
        import capo_securityhub.types.provider_summary

        out["provider_summary"] = (
            capo_securityhub.types.provider_summary.deserialize_json(
                data["ProviderSummary"]
            )
        )
    if "CreatedAt" in data:
        import capo_securityhub.types.timestamp

        out["created_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    return out
