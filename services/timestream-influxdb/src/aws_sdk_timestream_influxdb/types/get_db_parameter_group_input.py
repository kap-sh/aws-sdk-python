"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#GetDbParameterGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.db_parameter_group_identifier


class GetDbParameterGroupInput(TypedDict, closed=True):
    identifier: "aws_sdk_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
    """<p>The id of the DB parameter group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbParameterGroupInput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbParameterGroupInput:
    out: GetDbParameterGroupInput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("GetDbParameterGroupInput.identifier required")
    return out
