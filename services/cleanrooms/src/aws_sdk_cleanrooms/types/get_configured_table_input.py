"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetConfiguredTableInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_identifier


class GetConfiguredTableInput(TypedDict):
    configured_table_identifier: (
        "aws_sdk_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier"
    )
    """<p>The unique ID for the configured table to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredTableInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfiguredTableInput:
    out: GetConfiguredTableInput = {}  # type: ignore[typeddict-item]
    return out
