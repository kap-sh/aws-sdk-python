"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisErrorReason``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ephemeris_error_code
    import aws_sdk_groundstation.types.error_string


class EphemerisErrorReason(TypedDict, closed=True):
    error_code: "aws_sdk_groundstation.types.ephemeris_error_code.EphemerisErrorCode"
    r"""<p>The error code identifying the type of validation failure.</p> <p>See the <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/troubleshooting-invalid-ephemerides.html\">Troubleshooting Invalid Ephemerides guide</a> for error code details.</p>"""
    error_message: "aws_sdk_groundstation.types.error_string.ErrorString"
    """<p>A human-readable message describing the validation failure.</p> <p>Provides specific details about what failed and may include suggestions for remediation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisErrorReason) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.ephemeris_error_code

    out["errorCode"] = aws_sdk_groundstation.types.ephemeris_error_code.serialize_json(
        value["error_code"]
    )
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> EphemerisErrorReason:
    out: EphemerisErrorReason = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        import aws_sdk_groundstation.types.ephemeris_error_code

        out["error_code"] = (
            aws_sdk_groundstation.types.ephemeris_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        raise DeserializationError("EphemerisErrorReason.error_code required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("EphemerisErrorReason.error_message required")
    return out
