"""Generated from Smithy shape ``com.amazonaws.xray#ResponseTimeRootCauseEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_boolean
    import aws_sdk_xray.types.nullable_double
    import aws_sdk_xray.types.string


class ResponseTimeRootCauseEntity(TypedDict):
    name: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The name of the entity.</p>"""
    coverage: NotRequired["aws_sdk_xray.types.nullable_double.NullableDouble"]
    """<p>The type and messages of the exceptions.</p>"""
    remote: NotRequired["aws_sdk_xray.types.nullable_boolean.NullableBoolean"]
    """<p>A flag that denotes a remote subsegment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseTimeRootCauseEntity) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "coverage" in value:
        out["Coverage"] = value["coverage"]
    if "remote" in value:
        out["Remote"] = value["remote"]
    return out


def deserialize_json(data: dict) -> ResponseTimeRootCauseEntity:
    out: ResponseTimeRootCauseEntity = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Coverage" in data:
        out["coverage"] = data["Coverage"]
    if "Remote" in data:
        out["remote"] = data["Remote"]
    return out
