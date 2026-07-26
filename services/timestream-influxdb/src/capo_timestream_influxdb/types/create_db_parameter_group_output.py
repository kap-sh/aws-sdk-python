"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#CreateDbParameterGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.arn
    import capo_timestream_influxdb.types.db_parameter_group_id
    import capo_timestream_influxdb.types.db_parameter_group_name
    import capo_timestream_influxdb.types.parameters


class CreateDbParameterGroupOutput(TypedDict, closed=True):
    id: "capo_timestream_influxdb.types.db_parameter_group_id.DbParameterGroupId"
    """<p>A service-generated unique identifier.</p>"""
    name: "capo_timestream_influxdb.types.db_parameter_group_name.DbParameterGroupName"
    """<p>The customer-supplied name that uniquely identifies the DB parameter group when interacting with the Amazon Timestream for InfluxDB API and CLI commands.</p>"""
    arn: "capo_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARM) of the DB parameter group.</p>"""
    description: NotRequired["str"]
    """<p>The description of the DB parameter group.</p>"""
    parameters: NotRequired["capo_timestream_influxdb.types.parameters.Parameters"]
    """<p>A list of the parameters that comprise the DB parameter group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDbParameterGroupOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "parameters" in value:
        import capo_timestream_influxdb.types.parameters

        out["parameters"] = (
            capo_timestream_influxdb.types.parameters.serialize_aws_json_1_0(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDbParameterGroupOutput:
    out: CreateDbParameterGroupOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateDbParameterGroupOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDbParameterGroupOutput.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateDbParameterGroupOutput.arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "parameters" in data:
        import capo_timestream_influxdb.types.parameters

        out["parameters"] = (
            capo_timestream_influxdb.types.parameters.deserialize_aws_json_1_0(
                data["parameters"]
            )
        )
    return out
