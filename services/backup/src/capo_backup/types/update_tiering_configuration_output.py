"""Generated from Smithy shape ``com.amazonaws.backup#UpdateTieringConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.tiering_configuration_name
    import capo_backup.types.timestamp


class UpdateTieringConfigurationOutput(TypedDict, closed=True):
    tiering_configuration_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the updated tiering configuration.</p>"""
    tiering_configuration_name: NotRequired[
        "capo_backup.types.tiering_configuration_name.TieringConfigurationName"
    ]
    """<p>This unique string is the name of the tiering configuration.</p>"""
    creation_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time a tiering configuration was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.</p>"""
    last_updated_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time a tiering configuration was updated, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastUpdatedTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTieringConfigurationOutput) -> dict:
    out: dict = {}
    if "tiering_configuration_arn" in value:
        out["TieringConfigurationArn"] = value["tiering_configuration_arn"]
    if "tiering_configuration_name" in value:
        out["TieringConfigurationName"] = value["tiering_configuration_name"]
    if "creation_time" in value:
        import capo_backup.types.timestamp

        out["CreationTime"] = capo_backup.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_backup.types.timestamp

        out["LastUpdatedTime"] = capo_backup.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> UpdateTieringConfigurationOutput:
    out: UpdateTieringConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "TieringConfigurationArn" in data:
        out["tiering_configuration_arn"] = data["TieringConfigurationArn"]
    if "TieringConfigurationName" in data:
        out["tiering_configuration_name"] = data["TieringConfigurationName"]
    if "CreationTime" in data:
        import capo_backup.types.timestamp

        out["creation_time"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "LastUpdatedTime" in data:
        import capo_backup.types.timestamp

        out["last_updated_time"] = capo_backup.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    return out
