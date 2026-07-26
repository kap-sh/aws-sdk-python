"""Generated from Smithy shape ``com.amazonaws.wickr#NetworkSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.consent_popup_config
    import capo_wickr.types.read_receipt_config


class NetworkSettings(TypedDict, closed=True):
    enable_client_metrics: NotRequired["bool"]
    """<p>Allows Wickr clients to send anonymized performance and usage metrics to the Wickr backend server for service improvement and troubleshooting.</p>"""
    read_receipt_config: NotRequired[
        "capo_wickr.types.read_receipt_config.ReadReceiptConfig"
    ]
    """<p>Configuration for read receipts at the network level, controlling the default behavior for whether senders can see when their messages have been read.</p>"""
    data_retention: NotRequired["bool"]
    """<p>Indicates whether the data retention feature is enabled for the network. When true, messages are captured by the data retention bot for compliance and archiving purposes.</p>"""
    enable_trusted_data_format: NotRequired["bool"]
    """<p>Configuration for OpenTDF integration at the network level, enforcing ABAC decision making when operating in TDF enabled rooms.</p>"""
    consent_popup: NotRequired[
        "capo_wickr.types.consent_popup_config.ConsentPopupConfig"
    ]
    """<p>Consent popup configuration for the network, displayed to users on login.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkSettings) -> dict:
    out: dict = {}
    if "enable_client_metrics" in value:
        out["enableClientMetrics"] = value["enable_client_metrics"]
    if "read_receipt_config" in value:
        import capo_wickr.types.read_receipt_config

        out["readReceiptConfig"] = capo_wickr.types.read_receipt_config.serialize_json(
            value["read_receipt_config"]
        )
    if "data_retention" in value:
        out["dataRetention"] = value["data_retention"]
    if "enable_trusted_data_format" in value:
        out["enableTrustedDataFormat"] = value["enable_trusted_data_format"]
    if "consent_popup" in value:
        import capo_wickr.types.consent_popup_config

        out["consentPopup"] = capo_wickr.types.consent_popup_config.serialize_json(
            value["consent_popup"]
        )
    return out


def deserialize_json(data: dict) -> NetworkSettings:
    out: NetworkSettings = {}  # type: ignore[typeddict-item]
    if "enableClientMetrics" in data:
        out["enable_client_metrics"] = data["enableClientMetrics"]
    if "readReceiptConfig" in data:
        import capo_wickr.types.read_receipt_config

        out["read_receipt_config"] = (
            capo_wickr.types.read_receipt_config.deserialize_json(
                data["readReceiptConfig"]
            )
        )
    if "dataRetention" in data:
        out["data_retention"] = data["dataRetention"]
    if "enableTrustedDataFormat" in data:
        out["enable_trusted_data_format"] = data["enableTrustedDataFormat"]
    if "consentPopup" in data:
        import capo_wickr.types.consent_popup_config

        out["consent_popup"] = capo_wickr.types.consent_popup_config.deserialize_json(
            data["consentPopup"]
        )
    return out
