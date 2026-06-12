"""Generated from Smithy shape ``com.amazonaws.keyspaces#PointInTimeRecovery``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.point_in_time_recovery_status


class PointInTimeRecovery(TypedDict):
    status: "aws_sdk_keyspaces.types.point_in_time_recovery_status.PointInTimeRecoveryStatus"
    """<p>The options are:</p> <ul> <li> <p> <code>status=ENABLED</code> </p> </li> <li> <p> <code>status=DISABLED</code> </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PointInTimeRecovery) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PointInTimeRecovery:
    out: PointInTimeRecovery = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("PointInTimeRecovery.status required")
    return out
