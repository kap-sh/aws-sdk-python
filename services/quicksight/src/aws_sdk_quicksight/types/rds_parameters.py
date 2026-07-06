"""Generated from Smithy shape ``com.amazonaws.quicksight#RdsParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.database
    import aws_sdk_quicksight.types.instance_id


class RdsParameters(TypedDict, closed=True):
    instance_id: "aws_sdk_quicksight.types.instance_id.InstanceId"
    """<p>Instance ID.</p>"""
    database: "aws_sdk_quicksight.types.database.Database"
    """<p>Database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsParameters) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["Database"] = value["database"]
    return out


def deserialize_json(data: dict) -> RdsParameters:
    out: RdsParameters = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("RdsParameters.instance_id required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("RdsParameters.database required")
    return out
