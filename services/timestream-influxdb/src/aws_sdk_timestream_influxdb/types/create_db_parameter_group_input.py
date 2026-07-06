"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#CreateDbParameterGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.db_parameter_group_name
    import aws_sdk_timestream_influxdb.types.parameters
    import aws_sdk_timestream_influxdb.types.request_tag_map


class CreateDbParameterGroupInput(TypedDict, closed=True):
    name: (
        "aws_sdk_timestream_influxdb.types.db_parameter_group_name.DbParameterGroupName"
    )
    """<p>The name of the DB parameter group. The name must be unique per customer and per region.</p>"""
    description: NotRequired["str"]
    """<p>A description of the DB parameter group.</p>"""
    parameters: NotRequired["aws_sdk_timestream_influxdb.types.parameters.Parameters"]
    """<p>A list of the parameters that comprise the DB parameter group.</p>"""
    tags: NotRequired["aws_sdk_timestream_influxdb.types.request_tag_map.RequestTagMap"]
    """<p>A list of key-value pairs to associate with the DB parameter group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDbParameterGroupInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "parameters" in value:
        import aws_sdk_timestream_influxdb.types.parameters

        out["parameters"] = (
            aws_sdk_timestream_influxdb.types.parameters.serialize_aws_json_1_0(
                value["parameters"]
            )
        )
    if "tags" in value:
        import aws_sdk_timestream_influxdb.types.request_tag_map

        out["tags"] = (
            aws_sdk_timestream_influxdb.types.request_tag_map.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDbParameterGroupInput:
    out: CreateDbParameterGroupInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDbParameterGroupInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "parameters" in data:
        import aws_sdk_timestream_influxdb.types.parameters

        out["parameters"] = (
            aws_sdk_timestream_influxdb.types.parameters.deserialize_aws_json_1_0(
                data["parameters"]
            )
        )
    if "tags" in data:
        import aws_sdk_timestream_influxdb.types.request_tag_map

        out["tags"] = (
            aws_sdk_timestream_influxdb.types.request_tag_map.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
