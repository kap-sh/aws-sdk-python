"""Generated from Smithy shape ``com.amazonaws.drs#StopReplicationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.source_server


class StopReplicationResponse(TypedDict):
    source_server: NotRequired["aws_sdk_drs.types.source_server.SourceServer"]
    """<p>The Source Server that this action was targeted on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopReplicationResponse) -> dict:
    out: dict = {}
    if "source_server" in value:
        import aws_sdk_drs.types.source_server

        out["sourceServer"] = aws_sdk_drs.types.source_server.serialize_json(
            value["source_server"]
        )
    return out


def deserialize_json(data: dict) -> StopReplicationResponse:
    out: StopReplicationResponse = {}  # type: ignore[typeddict-item]
    if "sourceServer" in data:
        import aws_sdk_drs.types.source_server

        out["source_server"] = aws_sdk_drs.types.source_server.deserialize_json(
            data["sourceServer"]
        )
    return out
