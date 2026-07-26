"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#GetDbInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_instance_identifier


class GetDbInstanceInput(TypedDict, closed=True):
    identifier: (
        "capo_timestream_influxdb.types.db_instance_identifier.DbInstanceIdentifier"
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
