"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#CommandParameterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_jobs_data_plane.types.binary_parameter_value
    import capo_iot_jobs_data_plane.types.boolean_parameter_value
    import capo_iot_jobs_data_plane.types.double_parameter_value
    import capo_iot_jobs_data_plane.types.integer_parameter_value
    import capo_iot_jobs_data_plane.types.long_parameter_value
    import capo_iot_jobs_data_plane.types.string_parameter_value
    import capo_iot_jobs_data_plane.types.unsigned_long_parameter_value


class CommandParameterValue(TypedDict, closed=True):
    s: NotRequired[
        "capo_iot_jobs_data_plane.types.string_parameter_value.StringParameterValue"
    ]
    r"""<p>An attribute of type String. For example:</p> <p> <code>\"S\": \"Hello\"</code> </p>"""
    b: NotRequired[
        "capo_iot_jobs_data_plane.types.boolean_parameter_value.BooleanParameterValue"
    ]
    r"""<p>An attribute of type Boolean. For example:</p> <p> <code>\"BOOL\": true</code> </p>"""
    i: NotRequired[
        "capo_iot_jobs_data_plane.types.integer_parameter_value.IntegerParameterValue"
    ]
    """<p>An attribute of type Integer (Thirty-Two Bits).</p>"""
    l: NotRequired[
        "capo_iot_jobs_data_plane.types.long_parameter_value.LongParameterValue"
    ]
    """<p>An attribute of type Long.</p>"""
    d: NotRequired[
        "capo_iot_jobs_data_plane.types.double_parameter_value.DoubleParameterValue"
    ]
    """<p>An attribute of type Double (Sixty-Four Bits).</p>"""
    bin: NotRequired[
        "capo_iot_jobs_data_plane.types.binary_parameter_value.BinaryParameterValue"
    ]
    """<p>An attribute of type Binary.</p>"""
    ul: NotRequired[
        "capo_iot_jobs_data_plane.types.unsigned_long_parameter_value.UnsignedLongParameterValue"
    ]
    """<p>An attribute of type Unsigned Long.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandParameterValue) -> dict:
    out: dict = {}
    if "s" in value:
        out["S"] = value["s"]
    if "b" in value:
        out["B"] = value["b"]
    if "i" in value:
        out["I"] = value["i"]
    if "l" in value:
        out["L"] = value["l"]
    if "d" in value:
        out["D"] = value["d"]
    if "bin" in value:
        import capo_iot_jobs_data_plane.types.binary_parameter_value

        out["BIN"] = (
            capo_iot_jobs_data_plane.types.binary_parameter_value.serialize_json(
                value["bin"]
            )
        )
    if "ul" in value:
        out["UL"] = value["ul"]
    return out


def deserialize_json(data: dict) -> CommandParameterValue:
    out: CommandParameterValue = {}  # type: ignore[typeddict-item]
    if "S" in data:
        out["s"] = data["S"]
    if "B" in data:
        out["b"] = data["B"]
    if "I" in data:
        out["i"] = data["I"]
    if "L" in data:
        out["l"] = data["L"]
    if "D" in data:
        out["d"] = data["D"]
    if "BIN" in data:
        import capo_iot_jobs_data_plane.types.binary_parameter_value

        out["bin"] = (
            capo_iot_jobs_data_plane.types.binary_parameter_value.deserialize_json(
                data["BIN"]
            )
        )
    if "UL" in data:
        out["ul"] = data["UL"]
    return out
