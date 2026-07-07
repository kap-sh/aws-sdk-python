"""Generated from Smithy shape ``com.amazonaws.glue#CreateSecurityConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.timestamp_value


class CreateSecurityConfigurationResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name assigned to the new security configuration.</p>"""
    created_timestamp: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The time at which the new security configuration was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSecurityConfigurationResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "created_timestamp" in value:
        import aws_sdk_glue.types.timestamp_value

        out["CreatedTimestamp"] = (
            aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSecurityConfigurationResponse:
    out: CreateSecurityConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatedTimestamp" in data:
        import aws_sdk_glue.types.timestamp_value

        out["created_timestamp"] = (
            aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["CreatedTimestamp"]
            )
        )
    return out
