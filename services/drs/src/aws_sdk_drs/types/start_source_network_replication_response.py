"""Generated from Smithy shape ``com.amazonaws.drs#StartSourceNetworkReplicationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.source_network


class StartSourceNetworkReplicationResponse(TypedDict):
    source_network: NotRequired["aws_sdk_drs.types.source_network.SourceNetwork"]
    """<p>Source Network which was requested for replication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSourceNetworkReplicationResponse) -> dict:
    out: dict = {}
    if "source_network" in value:
        import aws_sdk_drs.types.source_network

        out["sourceNetwork"] = aws_sdk_drs.types.source_network.serialize_json(
            value["source_network"]
        )
    return out


def deserialize_json(data: dict) -> StartSourceNetworkReplicationResponse:
    out: StartSourceNetworkReplicationResponse = {}  # type: ignore[typeddict-item]
    if "sourceNetwork" in data:
        import aws_sdk_drs.types.source_network

        out["source_network"] = aws_sdk_drs.types.source_network.deserialize_json(
            data["sourceNetwork"]
        )
    return out
