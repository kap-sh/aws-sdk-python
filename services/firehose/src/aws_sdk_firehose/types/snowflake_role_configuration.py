"""Generated from Smithy shape ``com.amazonaws.firehose#SnowflakeRoleConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.boolean_object
    import aws_sdk_firehose.types.snowflake_role


class SnowflakeRoleConfiguration(TypedDict):
    enabled: NotRequired["aws_sdk_firehose.types.boolean_object.BooleanObject"]
    """<p>Enable Snowflake role</p>"""
    snowflake_role: NotRequired["aws_sdk_firehose.types.snowflake_role.SnowflakeRole"]
    """<p>The Snowflake role you wish to configure</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeRoleConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "snowflake_role" in value:
        out["SnowflakeRole"] = value["snowflake_role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowflakeRoleConfiguration:
    out: SnowflakeRoleConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "SnowflakeRole" in data:
        out["snowflake_role"] = data["SnowflakeRole"]
    return out
