"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalDecoder``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.can_signal
    import aws_sdk_iotfleetwise.types.custom_decoding_signal
    import aws_sdk_iotfleetwise.types.fully_qualified_name
    import aws_sdk_iotfleetwise.types.interface_id
    import aws_sdk_iotfleetwise.types.message_signal
    import aws_sdk_iotfleetwise.types.obd_signal
    import aws_sdk_iotfleetwise.types.signal_decoder_type


class SignalDecoder(TypedDict):
    fully_qualified_name: (
        "aws_sdk_iotfleetwise.types.fully_qualified_name.FullyQualifiedName"
    )
    """<p>The fully qualified name of a signal decoder as defined in a vehicle model.</p>"""
    type: "aws_sdk_iotfleetwise.types.signal_decoder_type.SignalDecoderType"
    """<p>The network protocol for the vehicle. For example, <code>CAN_SIGNAL</code> specifies a protocol that defines how data is communicated between electronic control units (ECUs). <code>OBD_SIGNAL</code> specifies a protocol that defines how self-diagnostic data is communicated between ECUs.</p>"""
    interface_id: "aws_sdk_iotfleetwise.types.interface_id.InterfaceId"
    """<p>The ID of a network interface that specifies what network protocol a vehicle follows.</p>"""
    can_signal: NotRequired["aws_sdk_iotfleetwise.types.can_signal.CanSignal"]
    """<p>Information about signal decoder using the Controller Area Network (CAN) protocol.</p>"""
    obd_signal: NotRequired["aws_sdk_iotfleetwise.types.obd_signal.ObdSignal"]
    """<p>Information about signal decoder using the on-board diagnostic (OBD) II protocol.</p>"""
    message_signal: NotRequired[
        "aws_sdk_iotfleetwise.types.message_signal.MessageSignal"
    ]
    """<p>The decoding information for a specific message which supports higher order data types. </p>"""
    custom_decoding_signal: NotRequired[
        "aws_sdk_iotfleetwise.types.custom_decoding_signal.CustomDecodingSignal"
    ]
    """<p>Information about a <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CustomDecodingSignal.html\">custom signal decoder</a>.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalDecoder) -> dict:
    out: dict = {}
    out["fullyQualifiedName"] = value["fully_qualified_name"]
    import aws_sdk_iotfleetwise.types.signal_decoder_type

    out["type"] = aws_sdk_iotfleetwise.types.signal_decoder_type.serialize_aws_json_1_0(
        value["type"]
    )
    out["interfaceId"] = value["interface_id"]
    if "can_signal" in value:
        import aws_sdk_iotfleetwise.types.can_signal

        out["canSignal"] = aws_sdk_iotfleetwise.types.can_signal.serialize_aws_json_1_0(
            value["can_signal"]
        )
    if "obd_signal" in value:
        import aws_sdk_iotfleetwise.types.obd_signal

        out["obdSignal"] = aws_sdk_iotfleetwise.types.obd_signal.serialize_aws_json_1_0(
            value["obd_signal"]
        )
    if "message_signal" in value:
        import aws_sdk_iotfleetwise.types.message_signal

        out["messageSignal"] = (
            aws_sdk_iotfleetwise.types.message_signal.serialize_aws_json_1_0(
                value["message_signal"]
            )
        )
    if "custom_decoding_signal" in value:
        import aws_sdk_iotfleetwise.types.custom_decoding_signal

        out["customDecodingSignal"] = (
            aws_sdk_iotfleetwise.types.custom_decoding_signal.serialize_aws_json_1_0(
                value["custom_decoding_signal"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SignalDecoder:
    out: SignalDecoder = {}  # type: ignore[typeddict-item]
    if "fullyQualifiedName" in data:
        out["fully_qualified_name"] = data["fullyQualifiedName"]
    else:
        raise DeserializationError("SignalDecoder.fully_qualified_name required")
    if "type" in data:
        import aws_sdk_iotfleetwise.types.signal_decoder_type

        out["type"] = (
            aws_sdk_iotfleetwise.types.signal_decoder_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    else:
        raise DeserializationError("SignalDecoder.type required")
    if "interfaceId" in data:
        out["interface_id"] = data["interfaceId"]
    else:
        raise DeserializationError("SignalDecoder.interface_id required")
    if "canSignal" in data:
        import aws_sdk_iotfleetwise.types.can_signal

        out["can_signal"] = (
            aws_sdk_iotfleetwise.types.can_signal.deserialize_aws_json_1_0(
                data["canSignal"]
            )
        )
    if "obdSignal" in data:
        import aws_sdk_iotfleetwise.types.obd_signal

        out["obd_signal"] = (
            aws_sdk_iotfleetwise.types.obd_signal.deserialize_aws_json_1_0(
                data["obdSignal"]
            )
        )
    if "messageSignal" in data:
        import aws_sdk_iotfleetwise.types.message_signal

        out["message_signal"] = (
            aws_sdk_iotfleetwise.types.message_signal.deserialize_aws_json_1_0(
                data["messageSignal"]
            )
        )
    if "customDecodingSignal" in data:
        import aws_sdk_iotfleetwise.types.custom_decoding_signal

        out["custom_decoding_signal"] = (
            aws_sdk_iotfleetwise.types.custom_decoding_signal.deserialize_aws_json_1_0(
                data["customDecodingSignal"]
            )
        )
    return out
