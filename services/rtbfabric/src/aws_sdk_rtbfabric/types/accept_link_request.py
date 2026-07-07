"""Generated from Smithy shape ``com.amazonaws.rtbfabric#AcceptLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_attributes
    import aws_sdk_rtbfabric.types.link_id
    import aws_sdk_rtbfabric.types.link_log_settings
    import aws_sdk_rtbfabric.types.link_timeout_in_millis


class AcceptLinkRequest(TypedDict, closed=True):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    attributes: NotRequired["aws_sdk_rtbfabric.types.link_attributes.LinkAttributes"]
    """<p>Attributes of the link.</p>"""
    log_settings: "aws_sdk_rtbfabric.types.link_log_settings.LinkLogSettings"
    """<p>Settings for the application logs.</p>"""
    timeout_in_millis: NotRequired[
        "aws_sdk_rtbfabric.types.link_timeout_in_millis.LinkTimeoutInMillis"
    ]
    """<p>The timeout value in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptLinkRequest) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_rtbfabric.types.link_attributes

        out["attributes"] = aws_sdk_rtbfabric.types.link_attributes.serialize_json(
            value["attributes"]
        )
    import aws_sdk_rtbfabric.types.link_log_settings

    out["logSettings"] = aws_sdk_rtbfabric.types.link_log_settings.serialize_json(
        value["log_settings"]
    )
    if "timeout_in_millis" in value:
        out["timeoutInMillis"] = value["timeout_in_millis"]
    return out


def deserialize_json(data: dict) -> AcceptLinkRequest:
    out: AcceptLinkRequest = {}  # type: ignore[typeddict-item]
    if "attributes" in data:
        import aws_sdk_rtbfabric.types.link_attributes

        out["attributes"] = aws_sdk_rtbfabric.types.link_attributes.deserialize_json(
            data["attributes"]
        )
    if "logSettings" in data:
        import aws_sdk_rtbfabric.types.link_log_settings

        out["log_settings"] = (
            aws_sdk_rtbfabric.types.link_log_settings.deserialize_json(
                data["logSettings"]
            )
        )
    else:
        raise DeserializationError("AcceptLinkRequest.log_settings required")
    if "timeoutInMillis" in data:
        out["timeout_in_millis"] = data["timeoutInMillis"]
    return out
