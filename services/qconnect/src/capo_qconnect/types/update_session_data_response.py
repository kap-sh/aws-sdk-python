"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateSessionDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.arn
    import capo_qconnect.types.runtime_session_data_list
    import capo_qconnect.types.session_data_namespace
    import capo_qconnect.types.uuid


class UpdateSessionDataResponse(TypedDict, closed=True):
    session_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    session_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the session.</p>"""
    namespace: "capo_qconnect.types.session_data_namespace.SessionDataNamespace"
    """<p>The namespace into which the session data is stored. Supported namespaces are: Custom</p>"""
    data: "capo_qconnect.types.runtime_session_data_list.RuntimeSessionDataList"
    """<p>Data stored in the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSessionDataResponse) -> dict:
    out: dict = {}
    out["sessionArn"] = value["session_arn"]
    out["sessionId"] = value["session_id"]
    out["namespace"] = value["namespace"]
    import capo_qconnect.types.runtime_session_data_list

    out["data"] = capo_qconnect.types.runtime_session_data_list.serialize_json(
        value["data"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSessionDataResponse:
    out: UpdateSessionDataResponse = {}  # type: ignore[typeddict-item]
    if "sessionArn" in data:
        out["session_arn"] = data["sessionArn"]
    else:
        raise DeserializationError("UpdateSessionDataResponse.session_arn required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("UpdateSessionDataResponse.session_id required")
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError("UpdateSessionDataResponse.namespace required")
    if "data" in data:
        import capo_qconnect.types.runtime_session_data_list

        out["data"] = capo_qconnect.types.runtime_session_data_list.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("UpdateSessionDataResponse.data required")
    return out
