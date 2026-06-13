"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#GetDbInstanceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.db_instance_identifier


class GetDbInstanceInput(TypedDict):
    identifier: (
        "aws_sdk_timestream_influxdb.types.db_instance_identifier.DbInstanceIdentifier"
    )
    """<p>The id of the DB instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbInstanceInput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbInstanceInput:
    out: GetDbInstanceInput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("GetDbInstanceInput.identifier required")
    return out
