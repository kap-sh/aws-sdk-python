"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateConfiguredTableOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table


class CreateConfiguredTableOutput(TypedDict, closed=True):
    configured_table: "aws_sdk_cleanrooms.types.configured_table.ConfiguredTable"
    """<p>The created configured table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredTableOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.configured_table

    out["configuredTable"] = aws_sdk_cleanrooms.types.configured_table.serialize_json(
        value["configured_table"]
    )
    return out


def deserialize_json(data: dict) -> CreateConfiguredTableOutput:
    out: CreateConfiguredTableOutput = {}  # type: ignore[typeddict-item]
    if "configuredTable" in data:
        import aws_sdk_cleanrooms.types.configured_table

        out["configured_table"] = (
            aws_sdk_cleanrooms.types.configured_table.deserialize_json(
                data["configuredTable"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConfiguredTableOutput.configured_table required"
        )
    return out
