"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbParameterGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.arn
    import capo_timestream_influxdb.types.db_parameter_group_id
    import capo_timestream_influxdb.types.db_parameter_group_name


class DbParameterGroupSummary(TypedDict, closed=True):
    id: "capo_timestream_influxdb.types.db_parameter_group_id.DbParameterGroupId"
    """<p>A service-generated unique identifier.</p>"""
    name: "capo_timestream_influxdb.types.db_parameter_group_name.DbParameterGroupName"
    """<p>This customer-supplied name uniquely identifies the parameter group.</p>"""
    arn: "capo_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the DB parameter group.</p>"""
    description: NotRequired["str"]
    """<p>A description of the DB parameter group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbParameterGroupSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DbParameterGroupSummary:
    out: DbParameterGroupSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DbParameterGroupSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DbParameterGroupSummary.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DbParameterGroupSummary.arn required")
    if "description" in data:
        out["description"] = data["description"]
    return out
