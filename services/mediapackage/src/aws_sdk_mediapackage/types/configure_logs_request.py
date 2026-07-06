"""Generated from Smithy shape ``com.amazonaws.mediapackage#ConfigureLogsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string
    import aws_sdk_mediapackage.types.egress_access_logs
    import aws_sdk_mediapackage.types.ingress_access_logs


class ConfigureLogsRequest(TypedDict, closed=True):
    egress_access_logs: NotRequired[
        "aws_sdk_mediapackage.types.egress_access_logs.EgressAccessLogs"
    ]
    id: "aws_sdk_mediapackage.types.__string.__string"
    """The ID of the channel to log subscription."""
    ingress_access_logs: NotRequired[
        "aws_sdk_mediapackage.types.ingress_access_logs.IngressAccessLogs"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureLogsRequest) -> dict:
    out: dict = {}
    if "egress_access_logs" in value:
        import aws_sdk_mediapackage.types.egress_access_logs

        out["egressAccessLogs"] = (
            aws_sdk_mediapackage.types.egress_access_logs.serialize_json(
                value["egress_access_logs"]
            )
        )
    if "ingress_access_logs" in value:
        import aws_sdk_mediapackage.types.ingress_access_logs

        out["ingressAccessLogs"] = (
            aws_sdk_mediapackage.types.ingress_access_logs.serialize_json(
                value["ingress_access_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigureLogsRequest:
    out: ConfigureLogsRequest = {}  # type: ignore[typeddict-item]
    if "egressAccessLogs" in data:
        import aws_sdk_mediapackage.types.egress_access_logs

        out["egress_access_logs"] = (
            aws_sdk_mediapackage.types.egress_access_logs.deserialize_json(
                data["egressAccessLogs"]
            )
        )
    if "ingressAccessLogs" in data:
        import aws_sdk_mediapackage.types.ingress_access_logs

        out["ingress_access_logs"] = (
            aws_sdk_mediapackage.types.ingress_access_logs.deserialize_json(
                data["ingressAccessLogs"]
            )
        )
    return out
