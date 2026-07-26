"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteConfiguredTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_identifier


class DeleteConfiguredTableInput(TypedDict, closed=True):
    configured_table_identifier: (
        "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier"
    )
    """<p>The unique ID for the configured table to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfiguredTableInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfiguredTableInput:
    out: DeleteConfiguredTableInput = {}  # type: ignore[typeddict-item]
    return out
