"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetConfiguredTableOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table


class GetConfiguredTableOutput(TypedDict):
    configured_table: "aws_sdk_cleanrooms.types.configured_table.ConfiguredTable"
    """<p>The retrieved configured table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredTableOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.configured_table

    out["configuredTable"] = aws_sdk_cleanrooms.types.configured_table.serialize_json(
        value["configured_table"]
    )
    return out


def deserialize_json(data: dict) -> GetConfiguredTableOutput:
    out: GetConfiguredTableOutput = {}  # type: ignore[typeddict-item]
    if "configuredTable" in data:
        import aws_sdk_cleanrooms.types.configured_table

        out["configured_table"] = (
            aws_sdk_cleanrooms.types.configured_table.deserialize_json(
                data["configuredTable"]
            )
        )
    else:
        raise DeserializationError("GetConfiguredTableOutput.configured_table required")
    return out
