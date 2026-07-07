"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ObdSignal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.double
    import aws_sdk_iotfleetwise.types.non_negative_integer
    import aws_sdk_iotfleetwise.types.obd_bitmask_length
    import aws_sdk_iotfleetwise.types.obd_byte_length
    import aws_sdk_iotfleetwise.types.positive_integer
    import aws_sdk_iotfleetwise.types.signal_value_type


class ObdSignal(TypedDict, closed=True):
    pid_response_length: "aws_sdk_iotfleetwise.types.positive_integer.positiveInteger"
    """<p>The length of the requested data.</p>"""
    service_mode: "aws_sdk_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>The mode of operation (diagnostic service) in a message.</p>"""
    pid: "aws_sdk_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>The diagnostic code used to request data from a vehicle for this signal.</p>"""
    scaling: "aws_sdk_iotfleetwise.types.double.double"
    """<p>A multiplier used to decode the message.</p>"""
    offset: "aws_sdk_iotfleetwise.types.double.double"
    """<p>The offset used to calculate the signal value. Combined with scaling, the calculation is <code>value = raw_value * scaling + offset</code>.</p>"""
    start_byte: "aws_sdk_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>Indicates the beginning of the message.</p>"""
    byte_length: "aws_sdk_iotfleetwise.types.obd_byte_length.ObdByteLength"
    """<p>The length of a message.</p>"""
    bit_right_shift: (
        "aws_sdk_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    )
    """<p>The number of positions to shift bits in the message.</p>"""
    bit_mask_length: NotRequired[
        "aws_sdk_iotfleetwise.types.obd_bitmask_length.ObdBitmaskLength"
    ]
    """<p>The number of bits to mask in a message.</p>"""
    is_signed: NotRequired["bool"]
    """<p>Determines whether the message is signed (<code>true</code>) or not (<code>false</code>). If it's signed, the message can represent both positive and negative numbers. The <code>isSigned</code> parameter only applies to the <code>INTEGER</code> raw signal type, and it doesn't affect the <code>FLOATING_POINT</code> raw signal type. The default value is <code>false</code>.</p>"""
    signal_value_type: NotRequired[
        "aws_sdk_iotfleetwise.types.signal_value_type.SignalValueType"
    ]
    """<p>The value type of the signal. The default value is <code>INTEGER</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ObdSignal) -> dict:
    out: dict = {}
    out["pidResponseLength"] = value["pid_response_length"]
    out["serviceMode"] = value.get("service_mode", 0)
    out["pid"] = value.get("pid", 0)
    out["scaling"] = value["scaling"]
    out["offset"] = value["offset"]
    out["startByte"] = value.get("start_byte", 0)
    out["byteLength"] = value["byte_length"]
    out["bitRightShift"] = value.get("bit_right_shift", 0)
    if "bit_mask_length" in value:
        out["bitMaskLength"] = value["bit_mask_length"]
    if "is_signed" in value:
        out["isSigned"] = value["is_signed"]
    if "signal_value_type" in value:
        import aws_sdk_iotfleetwise.types.signal_value_type

        out["signalValueType"] = (
            aws_sdk_iotfleetwise.types.signal_value_type.serialize_aws_json_1_0(
                value["signal_value_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ObdSignal:
    out: ObdSignal = {}  # type: ignore[typeddict-item]
    if "pidResponseLength" in data:
        out["pid_response_length"] = data["pidResponseLength"]
    else:
        raise DeserializationError("ObdSignal.pid_response_length required")
    if "serviceMode" in data:
        out["service_mode"] = data["serviceMode"]
    else:
        out["service_mode"] = 0
    if "pid" in data:
        out["pid"] = data["pid"]
    else:
        out["pid"] = 0
    if "scaling" in data:
        out["scaling"] = data["scaling"]
    else:
        raise DeserializationError("ObdSignal.scaling required")
    if "offset" in data:
        out["offset"] = data["offset"]
    else:
        raise DeserializationError("ObdSignal.offset required")
    if "startByte" in data:
        out["start_byte"] = data["startByte"]
    else:
        out["start_byte"] = 0
    if "byteLength" in data:
        out["byte_length"] = data["byteLength"]
    else:
        raise DeserializationError("ObdSignal.byte_length required")
    if "bitRightShift" in data:
        out["bit_right_shift"] = data["bitRightShift"]
    else:
        out["bit_right_shift"] = 0
    if "bitMaskLength" in data:
        out["bit_mask_length"] = data["bitMaskLength"]
    if "isSigned" in data:
        out["is_signed"] = data["isSigned"]
    if "signalValueType" in data:
        import aws_sdk_iotfleetwise.types.signal_value_type

        out["signal_value_type"] = (
            aws_sdk_iotfleetwise.types.signal_value_type.deserialize_aws_json_1_0(
                data["signalValueType"]
            )
        )
    return out
