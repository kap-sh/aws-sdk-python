"""Generated from Smithy shape ``com.amazonaws.glue#SecurityConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.encryption_configuration
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.timestamp_value


class SecurityConfiguration(TypedDict):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the security configuration.</p>"""
    created_time_stamp: NotRequired["aws_sdk_glue.types.timestamp_value.TimestampValue"]
    """<p>The time at which this security configuration was created.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_glue.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration associated with this security configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "created_time_stamp" in value:
        import aws_sdk_glue.types.timestamp_value

        out["CreatedTimeStamp"] = (
            aws_sdk_glue.types.timestamp_value.serialize_aws_json_1_1(
                value["created_time_stamp"]
            )
        )
    if "encryption_configuration" in value:
        import aws_sdk_glue.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            aws_sdk_glue.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SecurityConfiguration:
    out: SecurityConfiguration = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatedTimeStamp" in data:
        import aws_sdk_glue.types.timestamp_value

        out["created_time_stamp"] = (
            aws_sdk_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["CreatedTimeStamp"]
            )
        )
    if "EncryptionConfiguration" in data:
        import aws_sdk_glue.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_glue.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    return out
