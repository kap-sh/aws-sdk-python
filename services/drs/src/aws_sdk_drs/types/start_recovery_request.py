"""Generated from Smithy shape ``com.amazonaws.drs#StartRecoveryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.start_recovery_request_source_servers
    import aws_sdk_drs.types.tags_map


class StartRecoveryRequest(TypedDict, closed=True):
    source_servers: "aws_sdk_drs.types.start_recovery_request_source_servers.StartRecoveryRequestSourceServers"
    """<p>The Source Servers that we want to start a Recovery Job for.</p>"""
    is_drill: NotRequired["bool"]
    """<p>Whether this Source Server Recovery operation is a drill or not.</p>"""
    tags: NotRequired["aws_sdk_drs.types.tags_map.TagsMap"]
    """<p>The tags to be associated with the Recovery Job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRecoveryRequest) -> dict:
    out: dict = {}
    import aws_sdk_drs.types.start_recovery_request_source_servers

    out["sourceServers"] = (
        aws_sdk_drs.types.start_recovery_request_source_servers.serialize_json(
            value["source_servers"]
        )
    )
    if "is_drill" in value:
        out["isDrill"] = value["is_drill"]
    if "tags" in value:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartRecoveryRequest:
    out: StartRecoveryRequest = {}  # type: ignore[typeddict-item]
    if "sourceServers" in data:
        import aws_sdk_drs.types.start_recovery_request_source_servers

        out["source_servers"] = (
            aws_sdk_drs.types.start_recovery_request_source_servers.deserialize_json(
                data["sourceServers"]
            )
        )
    else:
        raise DeserializationError("StartRecoveryRequest.source_servers required")
    if "isDrill" in data:
        out["is_drill"] = data["isDrill"]
    if "tags" in data:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.deserialize_json(data["tags"])
    return out
