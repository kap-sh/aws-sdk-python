"""Generated from Smithy shape ``com.amazonaws.qconnect#RuntimeSessionData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_sensitive_string
    import aws_sdk_qconnect.types.runtime_session_data_value


class RuntimeSessionData(TypedDict, closed=True):
    key: "aws_sdk_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    """<p>The key of the data stored on the session.</p>"""
    value: "aws_sdk_qconnect.types.runtime_session_data_value.RuntimeSessionDataValue"
    """<p>The value of the data stored on the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeSessionData) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import aws_sdk_qconnect.types.runtime_session_data_value

    out["value"] = aws_sdk_qconnect.types.runtime_session_data_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> RuntimeSessionData:
    out: RuntimeSessionData = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("RuntimeSessionData.key required")
    if "value" in data:
        import aws_sdk_qconnect.types.runtime_session_data_value

        out["value"] = (
            aws_sdk_qconnect.types.runtime_session_data_value.deserialize_json(
                data["value"]
            )
        )
    else:
        raise DeserializationError("RuntimeSessionData.value required")
    return out
