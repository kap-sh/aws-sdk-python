"""Generated from Smithy shape ``com.amazonaws.xray#FaultRootCauseEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_boolean
    import aws_sdk_xray.types.root_cause_exceptions
    import aws_sdk_xray.types.string


class FaultRootCauseEntity(TypedDict, closed=True):
    name: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The name of the entity.</p>"""
    exceptions: NotRequired[
        "aws_sdk_xray.types.root_cause_exceptions.RootCauseExceptions"
    ]
    """<p>The types and messages of the exceptions.</p>"""
    remote: NotRequired["aws_sdk_xray.types.nullable_boolean.NullableBoolean"]
    """<p>A flag that denotes a remote subsegment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FaultRootCauseEntity) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "exceptions" in value:
        import aws_sdk_xray.types.root_cause_exceptions

        out["Exceptions"] = aws_sdk_xray.types.root_cause_exceptions.serialize_json(
            value["exceptions"]
        )
    if "remote" in value:
        out["Remote"] = value["remote"]
    return out


def deserialize_json(data: dict) -> FaultRootCauseEntity:
    out: FaultRootCauseEntity = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Exceptions" in data:
        import aws_sdk_xray.types.root_cause_exceptions

        out["exceptions"] = aws_sdk_xray.types.root_cause_exceptions.deserialize_json(
            data["Exceptions"]
        )
    if "Remote" in data:
        out["remote"] = data["Remote"]
    return out
