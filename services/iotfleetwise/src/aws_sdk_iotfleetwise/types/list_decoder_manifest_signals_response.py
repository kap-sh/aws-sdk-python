"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListDecoderManifestSignalsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.next_token
    import aws_sdk_iotfleetwise.types.signal_decoders


class ListDecoderManifestSignalsResponse(TypedDict):
    signal_decoders: NotRequired[
        "aws_sdk_iotfleetwise.types.signal_decoders.SignalDecoders"
    ]
    """<p> Information about a list of signals to decode. </p>"""
    next_token: NotRequired["aws_sdk_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDecoderManifestSignalsResponse) -> dict:
    out: dict = {}
    if "signal_decoders" in value:
        import aws_sdk_iotfleetwise.types.signal_decoders

        out["signalDecoders"] = (
            aws_sdk_iotfleetwise.types.signal_decoders.serialize_aws_json_1_0(
                value["signal_decoders"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDecoderManifestSignalsResponse:
    out: ListDecoderManifestSignalsResponse = {}  # type: ignore[typeddict-item]
    if "signalDecoders" in data:
        import aws_sdk_iotfleetwise.types.signal_decoders

        out["signal_decoders"] = (
            aws_sdk_iotfleetwise.types.signal_decoders.deserialize_aws_json_1_0(
                data["signalDecoders"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
