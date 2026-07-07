"""Generated from Smithy shape ``com.amazonaws.panorama#SignalApplicationInstanceNodeInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.application_instance_id
    import aws_sdk_panorama.types.node_signal_list


class SignalApplicationInstanceNodeInstancesRequest(TypedDict, closed=True):
    application_instance_id: (
        "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId"
    )
    """<p>An application instance ID.</p>"""
    node_signals: "aws_sdk_panorama.types.node_signal_list.NodeSignalList"
    """<p>A list of signals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignalApplicationInstanceNodeInstancesRequest) -> dict:
    out: dict = {}
    import aws_sdk_panorama.types.node_signal_list

    out["NodeSignals"] = aws_sdk_panorama.types.node_signal_list.serialize_json(
        value["node_signals"]
    )
    return out


def deserialize_json(data: dict) -> SignalApplicationInstanceNodeInstancesRequest:
    out: SignalApplicationInstanceNodeInstancesRequest = {}  # type: ignore[typeddict-item]
    if "NodeSignals" in data:
        import aws_sdk_panorama.types.node_signal_list

        out["node_signals"] = aws_sdk_panorama.types.node_signal_list.deserialize_json(
            data["NodeSignals"]
        )
    else:
        raise DeserializationError(
            "SignalApplicationInstanceNodeInstancesRequest.node_signals required"
        )
    return out
