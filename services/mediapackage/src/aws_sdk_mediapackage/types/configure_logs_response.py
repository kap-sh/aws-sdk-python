"""Generated from Smithy shape ``com.amazonaws.mediapackage#ConfigureLogsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string
    import aws_sdk_mediapackage.types.egress_access_logs
    import aws_sdk_mediapackage.types.hls_ingest
    import aws_sdk_mediapackage.types.ingress_access_logs
    import aws_sdk_mediapackage.types.tags


class ConfigureLogsResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The Amazon Resource Name (ARN) assigned to the Channel."""
    created_at: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The date and time the Channel was created."""
    description: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """A short text description of the Channel."""
    egress_access_logs: NotRequired[
        "aws_sdk_mediapackage.types.egress_access_logs.EgressAccessLogs"
    ]
    hls_ingest: NotRequired["aws_sdk_mediapackage.types.hls_ingest.HlsIngest"]
    id: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The ID of the Channel."""
    ingress_access_logs: NotRequired[
        "aws_sdk_mediapackage.types.ingress_access_logs.IngressAccessLogs"
    ]
    tags: NotRequired["aws_sdk_mediapackage.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureLogsResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "description" in value:
        out["description"] = value["description"]
    if "egress_access_logs" in value:
        import aws_sdk_mediapackage.types.egress_access_logs

        out["egressAccessLogs"] = (
            aws_sdk_mediapackage.types.egress_access_logs.serialize_json(
                value["egress_access_logs"]
            )
        )
    if "hls_ingest" in value:
        import aws_sdk_mediapackage.types.hls_ingest

        out["hlsIngest"] = aws_sdk_mediapackage.types.hls_ingest.serialize_json(
            value["hls_ingest"]
        )
    if "id" in value:
        out["id"] = value["id"]
    if "ingress_access_logs" in value:
        import aws_sdk_mediapackage.types.ingress_access_logs

        out["ingressAccessLogs"] = (
            aws_sdk_mediapackage.types.ingress_access_logs.serialize_json(
                value["ingress_access_logs"]
            )
        )
    if "tags" in value:
        import aws_sdk_mediapackage.types.tags

        out["tags"] = aws_sdk_mediapackage.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ConfigureLogsResponse:
    out: ConfigureLogsResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    if "description" in data:
        out["description"] = data["description"]
    if "egressAccessLogs" in data:
        import aws_sdk_mediapackage.types.egress_access_logs

        out["egress_access_logs"] = (
            aws_sdk_mediapackage.types.egress_access_logs.deserialize_json(
                data["egressAccessLogs"]
            )
        )
    if "hlsIngest" in data:
        import aws_sdk_mediapackage.types.hls_ingest

        out["hls_ingest"] = aws_sdk_mediapackage.types.hls_ingest.deserialize_json(
            data["hlsIngest"]
        )
    if "id" in data:
        out["id"] = data["id"]
    if "ingressAccessLogs" in data:
        import aws_sdk_mediapackage.types.ingress_access_logs

        out["ingress_access_logs"] = (
            aws_sdk_mediapackage.types.ingress_access_logs.deserialize_json(
                data["ingressAccessLogs"]
            )
        )
    if "tags" in data:
        import aws_sdk_mediapackage.types.tags

        out["tags"] = aws_sdk_mediapackage.types.tags.deserialize_json(data["tags"])
    return out
