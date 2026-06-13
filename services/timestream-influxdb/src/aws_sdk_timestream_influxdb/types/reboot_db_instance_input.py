"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#RebootDbInstanceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.db_instance_identifier


class RebootDbInstanceInput(TypedDict):
    identifier: (
        "aws_sdk_timestream_influxdb.types.db_instance_identifier.DbInstanceIdentifier"
    )
    """<p>The id of the DB instance to reboot.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RebootDbInstanceInput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RebootDbInstanceInput:
    out: RebootDbInstanceInput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("RebootDbInstanceInput.identifier required")
    return out
