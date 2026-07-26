"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateConfiguredTableOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table


class UpdateConfiguredTableOutput(TypedDict, closed=True):
    configured_table: "capo_cleanrooms.types.configured_table.ConfiguredTable"
    """<p>The updated configured table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredTableOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.configured_table

    out["configuredTable"] = capo_cleanrooms.types.configured_table.serialize_json(
        value["configured_table"]
    )
    return out


def deserialize_json(data: dict) -> UpdateConfiguredTableOutput:
    out: UpdateConfiguredTableOutput = {}  # type: ignore[typeddict-item]
    if "configuredTable" in data:
        import capo_cleanrooms.types.configured_table

        out["configured_table"] = (
            capo_cleanrooms.types.configured_table.deserialize_json(
                data["configuredTable"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConfiguredTableOutput.configured_table required"
        )
    return out
