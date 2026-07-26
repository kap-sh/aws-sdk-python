"""Generated from Smithy shape ``com.amazonaws.qconnect#RuntimeSessionData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_sensitive_string
    import capo_qconnect.types.runtime_session_data_value


class RuntimeSessionData(TypedDict, closed=True):
    key: "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    """<p>The key of the data stored on the session.</p>"""
    value: "capo_qconnect.types.runtime_session_data_value.RuntimeSessionDataValue"
    """<p>The value of the data stored on the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeSessionData) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_qconnect.types.runtime_session_data_value

    out["value"] = capo_qconnect.types.runtime_session_data_value.serialize_json(
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
        import capo_qconnect.types.runtime_session_data_value

        out["value"] = capo_qconnect.types.runtime_session_data_value.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("RuntimeSessionData.value required")
    return out
