"""Generated from Smithy shape ``com.amazonaws.backup#UpdateTieringConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.tiering_configuration_input_for_update
    import capo_backup.types.tiering_configuration_name


class UpdateTieringConfigurationInput(TypedDict, closed=True):
    tiering_configuration_name: (
        "capo_backup.types.tiering_configuration_name.TieringConfigurationName"
    )
    """<p>The name of a tiering configuration to update.</p>"""
    tiering_configuration: "capo_backup.types.tiering_configuration_input_for_update.TieringConfigurationInputForUpdate"
    """<p>Specifies the body of a tiering configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTieringConfigurationInput) -> dict:
    out: dict = {}
    import capo_backup.types.tiering_configuration_input_for_update

    out["TieringConfiguration"] = (
        capo_backup.types.tiering_configuration_input_for_update.serialize_json(
            value["tiering_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateTieringConfigurationInput:
    out: UpdateTieringConfigurationInput = {}  # type: ignore[typeddict-item]
    if "TieringConfiguration" in data:
        import capo_backup.types.tiering_configuration_input_for_update

        out["tiering_configuration"] = (
            capo_backup.types.tiering_configuration_input_for_update.deserialize_json(
                data["TieringConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTieringConfigurationInput.tiering_configuration required"
        )
    return out
