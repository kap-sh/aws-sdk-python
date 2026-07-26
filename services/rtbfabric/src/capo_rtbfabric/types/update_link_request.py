"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.link_id
    import capo_rtbfabric.types.link_log_settings
    import capo_rtbfabric.types.link_timeout_in_millis


class UpdateLinkRequest(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    log_settings: NotRequired["capo_rtbfabric.types.link_log_settings.LinkLogSettings"]
    """<p>Settings for the application logs.</p>"""
    timeout_in_millis: NotRequired[
        "capo_rtbfabric.types.link_timeout_in_millis.LinkTimeoutInMillis"
    ]
    """<p>The timeout value in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkRequest) -> dict:
    out: dict = {}
    if "log_settings" in value:
        import capo_rtbfabric.types.link_log_settings

        out["logSettings"] = capo_rtbfabric.types.link_log_settings.serialize_json(
            value["log_settings"]
        )
    if "timeout_in_millis" in value:
        out["timeoutInMillis"] = value["timeout_in_millis"]
    return out


def deserialize_json(data: dict) -> UpdateLinkRequest:
    out: UpdateLinkRequest = {}  # type: ignore[typeddict-item]
    if "logSettings" in data:
        import capo_rtbfabric.types.link_log_settings

        out["log_settings"] = capo_rtbfabric.types.link_log_settings.deserialize_json(
            data["logSettings"]
        )
    if "timeoutInMillis" in data:
        out["timeout_in_millis"] = data["timeoutInMillis"]
    return out
