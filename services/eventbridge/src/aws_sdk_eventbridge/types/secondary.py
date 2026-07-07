"""Generated from Smithy shape ``com.amazonaws.eventbridge#Secondary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.route


class Secondary(TypedDict, closed=True):
    route: "aws_sdk_eventbridge.types.route.Route"
    """<p>Defines the secondary Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Secondary) -> dict:
    out: dict = {}
    out["Route"] = value["route"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Secondary:
    out: Secondary = {}  # type: ignore[typeddict-item]
    if "Route" in data:
        out["route"] = data["Route"]
    else:
        raise DeserializationError("Secondary.route required")
    return out
