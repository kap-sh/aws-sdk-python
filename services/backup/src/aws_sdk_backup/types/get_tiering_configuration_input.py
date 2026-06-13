"""Generated from Smithy shape ``com.amazonaws.backup#GetTieringConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.tiering_configuration_name


class GetTieringConfigurationInput(TypedDict):
    tiering_configuration_name: (
        "aws_sdk_backup.types.tiering_configuration_name.TieringConfigurationName"
    )
    """<p>The unique name of a tiering configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTieringConfigurationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTieringConfigurationInput:
    out: GetTieringConfigurationInput = {}  # type: ignore[typeddict-item]
    return out
