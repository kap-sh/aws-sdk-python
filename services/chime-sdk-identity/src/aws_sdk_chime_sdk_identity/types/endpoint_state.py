"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#EndpointState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.endpoint_status
    import aws_sdk_chime_sdk_identity.types.endpoint_status_reason


class EndpointState(TypedDict, closed=True):
    status: "aws_sdk_chime_sdk_identity.types.endpoint_status.EndpointStatus"
    """<p>Enum that indicates the Status of an <code>AppInstanceUserEndpoint</code>.</p>"""
    status_reason: NotRequired[
        "aws_sdk_chime_sdk_identity.types.endpoint_status_reason.EndpointStatusReason"
    ]
    """<p>The reason for the <code>EndpointStatus</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointState) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_identity.types.endpoint_status

    out["Status"] = aws_sdk_chime_sdk_identity.types.endpoint_status.serialize_json(
        value["status"]
    )
    if "status_reason" in value:
        import aws_sdk_chime_sdk_identity.types.endpoint_status_reason

        out["StatusReason"] = (
            aws_sdk_chime_sdk_identity.types.endpoint_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> EndpointState:
    out: EndpointState = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_chime_sdk_identity.types.endpoint_status

        out["status"] = (
            aws_sdk_chime_sdk_identity.types.endpoint_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("EndpointState.status required")
    if "StatusReason" in data:
        import aws_sdk_chime_sdk_identity.types.endpoint_status_reason

        out["status_reason"] = (
            aws_sdk_chime_sdk_identity.types.endpoint_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    return out
