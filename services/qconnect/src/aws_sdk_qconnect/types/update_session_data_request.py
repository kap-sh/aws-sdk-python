"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateSessionDataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.runtime_session_data_list
    import aws_sdk_qconnect.types.session_data_namespace
    import aws_sdk_qconnect.types.uuid_or_arn


class UpdateSessionDataRequest(TypedDict):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    session_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    namespace: NotRequired[
        "aws_sdk_qconnect.types.session_data_namespace.SessionDataNamespace"
    ]
    """<p>The namespace into which the session data is stored. Supported namespaces are: Custom</p>"""
    data: "aws_sdk_qconnect.types.runtime_session_data_list.RuntimeSessionDataList"
    """<p>The data stored on the Amazon Q in Connect Session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSessionDataRequest) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    import aws_sdk_qconnect.types.runtime_session_data_list

    out["data"] = aws_sdk_qconnect.types.runtime_session_data_list.serialize_json(
        value["data"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSessionDataRequest:
    out: UpdateSessionDataRequest = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "data" in data:
        import aws_sdk_qconnect.types.runtime_session_data_list

        out["data"] = aws_sdk_qconnect.types.runtime_session_data_list.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("UpdateSessionDataRequest.data required")
    return out
