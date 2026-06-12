"""Generated from Smithy shape ``com.amazonaws.securityhub#ProviderSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.connector_provider_name
    import aws_sdk_securityhub.types.connector_status


class ProviderSummary(TypedDict):
    provider_name: NotRequired[
        "aws_sdk_securityhub.types.connector_provider_name.ConnectorProviderName"
    ]
    """<p>The name of the provider.</p>"""
    connector_status: NotRequired[
        "aws_sdk_securityhub.types.connector_status.ConnectorStatus"
    ]
    """<p>The status for the connectorV2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderSummary) -> dict:
    out: dict = {}
    if "provider_name" in value:
        import aws_sdk_securityhub.types.connector_provider_name

        out["ProviderName"] = (
            aws_sdk_securityhub.types.connector_provider_name.serialize_json(
                value["provider_name"]
            )
        )
    if "connector_status" in value:
        import aws_sdk_securityhub.types.connector_status

        out["ConnectorStatus"] = (
            aws_sdk_securityhub.types.connector_status.serialize_json(
                value["connector_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProviderSummary:
    out: ProviderSummary = {}  # type: ignore[typeddict-item]
    if "ProviderName" in data:
        import aws_sdk_securityhub.types.connector_provider_name

        out["provider_name"] = (
            aws_sdk_securityhub.types.connector_provider_name.deserialize_json(
                data["ProviderName"]
            )
        )
    if "ConnectorStatus" in data:
        import aws_sdk_securityhub.types.connector_status

        out["connector_status"] = (
            aws_sdk_securityhub.types.connector_status.deserialize_json(
                data["ConnectorStatus"]
            )
        )
    return out
