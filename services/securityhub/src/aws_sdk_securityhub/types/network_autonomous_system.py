"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkAutonomousSystem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class NetworkAutonomousSystem(TypedDict, closed=True):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name associated with the AS. </p>"""
    number: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The unique number that identifies the AS. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkAutonomousSystem) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "number" in value:
        out["Number"] = value["number"]
    return out


def deserialize_json(data: dict) -> NetworkAutonomousSystem:
    out: NetworkAutonomousSystem = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Number" in data:
        out["number"] = data["Number"]
    return out
