"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListDecoderManifestSignalsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.next_token
    import capo_iotfleetwise.types.signal_decoders


class ListDecoderManifestSignalsResponse(TypedDict, closed=True):
    signal_decoders: NotRequired[
        "capo_iotfleetwise.types.signal_decoders.SignalDecoders"
    ]
    """<p> Information about a list of signals to decode. </p>"""
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDecoderManifestSignalsResponse) -> dict:
    out: dict = {}
    if "signal_decoders" in value:
        import capo_iotfleetwise.types.signal_decoders

        out["signalDecoders"] = (
            capo_iotfleetwise.types.signal_decoders.serialize_aws_json_1_0(
                value["signal_decoders"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDecoderManifestSignalsResponse:
    out: ListDecoderManifestSignalsResponse = {}  # type: ignore[typeddict-item]
    if "signalDecoders" in data:
        import capo_iotfleetwise.types.signal_decoders

        out["signal_decoders"] = (
            capo_iotfleetwise.types.signal_decoders.deserialize_aws_json_1_0(
                data["signalDecoders"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
