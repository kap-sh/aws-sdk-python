"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CanSignal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.can_signal_name
    import aws_sdk_iotfleetwise.types.double
    import aws_sdk_iotfleetwise.types.non_negative_integer
    import aws_sdk_iotfleetwise.types.signal_value_type


class CanSignal(TypedDict, closed=True):
    message_id: "aws_sdk_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>The ID of the message.</p>"""
    is_big_endian: "bool"
    """<p>Whether the byte ordering of a CAN message is big-endian.</p>"""
    is_signed: "bool"
    """<p>Determines whether the message is signed (<code>true</code>) or not (<code>false</code>). If it's signed, the message can represent both positive and negative numbers. The <code>isSigned</code> parameter only applies to the <code>INTEGER</code> raw signal type, and it doesn't affect the <code>FLOATING_POINT</code> raw signal type.</p>"""
    start_bit: "aws_sdk_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>Indicates the beginning of the CAN signal. This should always be the least significant bit (LSB).</p> <p>This value might be different from the value in a DBC file. For little endian signals, <code>startBit</code> is the same value as in the DBC file. For big endian signals in a DBC file, the start bit is the most significant bit (MSB). You will have to calculate the LSB instead and pass it as the <code>startBit</code>.</p>"""
    offset: "aws_sdk_iotfleetwise.types.double.double"
    """<p>The offset used to calculate the signal value. Combined with factor, the calculation is <code>value = raw_value * factor + offset</code>.</p>"""
    factor: "aws_sdk_iotfleetwise.types.double.double"
    """<p>A multiplier used to decode the CAN message.</p>"""
    length: "aws_sdk_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>How many bytes of data are in the message.</p>"""
    name: NotRequired["aws_sdk_iotfleetwise.types.can_signal_name.CanSignalName"]
    """<p>The name of the signal.</p>"""
    signal_value_type: NotRequired[
        "aws_sdk_iotfleetwise.types.signal_value_type.SignalValueType"
    ]
    """<p>The value type of the signal. The default value is <code>INTEGER</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CanSignal) -> dict:
    out: dict = {}
    out["messageId"] = value.get("message_id", 0)
    out["isBigEndian"] = value.get("is_big_endian", False)
    out["isSigned"] = value.get("is_signed", False)
    out["startBit"] = value.get("start_bit", 0)
    out["offset"] = value["offset"]
    out["factor"] = value["factor"]
    out["length"] = value.get("length", 0)
    if "name" in value:
        out["name"] = value["name"]
    if "signal_value_type" in value:
        import aws_sdk_iotfleetwise.types.signal_value_type

        out["signalValueType"] = (
            aws_sdk_iotfleetwise.types.signal_value_type.serialize_aws_json_1_0(
                value["signal_value_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CanSignal:
    out: CanSignal = {}  # type: ignore[typeddict-item]
    if "messageId" in data:
        out["message_id"] = data["messageId"]
    else:
        out["message_id"] = 0
    if "isBigEndian" in data:
        out["is_big_endian"] = data["isBigEndian"]
    else:
        out["is_big_endian"] = False
    if "isSigned" in data:
        out["is_signed"] = data["isSigned"]
    else:
        out["is_signed"] = False
    if "startBit" in data:
        out["start_bit"] = data["startBit"]
    else:
        out["start_bit"] = 0
    if "offset" in data:
        out["offset"] = data["offset"]
    else:
        raise DeserializationError("CanSignal.offset required")
    if "factor" in data:
        out["factor"] = data["factor"]
    else:
        raise DeserializationError("CanSignal.factor required")
    if "length" in data:
        out["length"] = data["length"]
    else:
        out["length"] = 0
    if "name" in data:
        out["name"] = data["name"]
    if "signalValueType" in data:
        import aws_sdk_iotfleetwise.types.signal_value_type

        out["signal_value_type"] = (
            aws_sdk_iotfleetwise.types.signal_value_type.deserialize_aws_json_1_0(
                data["signalValueType"]
            )
        )
    return out
