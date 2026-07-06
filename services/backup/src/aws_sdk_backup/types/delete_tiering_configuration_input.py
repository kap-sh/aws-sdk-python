"""Generated from Smithy shape ``com.amazonaws.backup#DeleteTieringConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.tiering_configuration_name


class DeleteTieringConfigurationInput(TypedDict, closed=True):
    tiering_configuration_name: (
        "aws_sdk_backup.types.tiering_configuration_name.TieringConfigurationName"
    )
    """<p>The unique name of a tiering configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTieringConfigurationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTieringConfigurationInput:
    out: DeleteTieringConfigurationInput = {}  # type: ignore[typeddict-item]
    return out
