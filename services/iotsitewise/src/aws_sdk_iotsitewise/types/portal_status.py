"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PortalStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.monitor_error_details
    import aws_sdk_iotsitewise.types.portal_state


class PortalStatus(TypedDict):
    state: "aws_sdk_iotsitewise.types.portal_state.PortalState"
    """<p>The current state of the portal.</p>"""
    error: NotRequired[
        "aws_sdk_iotsitewise.types.monitor_error_details.MonitorErrorDetails"
    ]
    """<p>Contains associated error information, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortalStatus) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.portal_state

    out["state"] = aws_sdk_iotsitewise.types.portal_state.serialize_json(value["state"])
    if "error" in value:
        import aws_sdk_iotsitewise.types.monitor_error_details

        out["error"] = aws_sdk_iotsitewise.types.monitor_error_details.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> PortalStatus:
    out: PortalStatus = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_iotsitewise.types.portal_state

        out["state"] = aws_sdk_iotsitewise.types.portal_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("PortalStatus.state required")
    if "error" in data:
        import aws_sdk_iotsitewise.types.monitor_error_details

        out["error"] = aws_sdk_iotsitewise.types.monitor_error_details.deserialize_json(
            data["error"]
        )
    return out
