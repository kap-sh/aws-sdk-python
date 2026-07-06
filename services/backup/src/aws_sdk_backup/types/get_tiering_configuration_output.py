"""Generated from Smithy shape ``com.amazonaws.backup#GetTieringConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.tiering_configuration


class GetTieringConfigurationOutput(TypedDict, closed=True):
    tiering_configuration: NotRequired[
        "aws_sdk_backup.types.tiering_configuration.TieringConfiguration"
    ]
    """<p>Specifies the body of a tiering configuration. Includes <code>TieringConfigurationName</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTieringConfigurationOutput) -> dict:
    out: dict = {}
    if "tiering_configuration" in value:
        import aws_sdk_backup.types.tiering_configuration

        out["TieringConfiguration"] = (
            aws_sdk_backup.types.tiering_configuration.serialize_json(
                value["tiering_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTieringConfigurationOutput:
    out: GetTieringConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "TieringConfiguration" in data:
        import aws_sdk_backup.types.tiering_configuration

        out["tiering_configuration"] = (
            aws_sdk_backup.types.tiering_configuration.deserialize_json(
                data["TieringConfiguration"]
            )
        )
    return out
