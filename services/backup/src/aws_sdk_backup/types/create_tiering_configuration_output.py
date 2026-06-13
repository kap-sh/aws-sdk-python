"""Generated from Smithy shape ``com.amazonaws.backup#CreateTieringConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class CreateTieringConfigurationOutput(TypedDict):
    tiering_configuration_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the created tiering configuration.</p>"""
    tiering_configuration_name: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>This unique string is the name of the tiering configuration.</p> <p>The name cannot be changed after creation. The name consists of only alphanumeric characters and underscores. Maximum length is 200.</p>"""
    creation_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time a tiering configuration was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTieringConfigurationOutput) -> dict:
    out: dict = {}
    if "tiering_configuration_arn" in value:
        out["TieringConfigurationArn"] = value["tiering_configuration_arn"]
    if "tiering_configuration_name" in value:
        out["TieringConfigurationName"] = value["tiering_configuration_name"]
    if "creation_time" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationTime"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_time"]
        )
    return out


def deserialize_json(data: dict) -> CreateTieringConfigurationOutput:
    out: CreateTieringConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "TieringConfigurationArn" in data:
        out["tiering_configuration_arn"] = data["TieringConfigurationArn"]
    if "TieringConfigurationName" in data:
        out["tiering_configuration_name"] = data["TieringConfigurationName"]
    if "CreationTime" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_time"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    return out
