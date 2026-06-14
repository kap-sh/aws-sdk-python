"""Generated from Smithy shape ``com.amazonaws.datazone#GluePropertiesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.glue_connection_input


class GluePropertiesInput(TypedDict):
    glue_connection_input: NotRequired[
        "aws_sdk_datazone.types.glue_connection_input.GlueConnectionInput"
    ]
    """<p>The Amazon Web Services Glue connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GluePropertiesInput) -> dict:
    out: dict = {}
    if "glue_connection_input" in value:
        import aws_sdk_datazone.types.glue_connection_input

        out["glueConnectionInput"] = (
            aws_sdk_datazone.types.glue_connection_input.serialize_json(
                value["glue_connection_input"]
            )
        )
    return out


def deserialize_json(data: dict) -> GluePropertiesInput:
    out: GluePropertiesInput = {}  # type: ignore[typeddict-item]
    if "glueConnectionInput" in data:
        import aws_sdk_datazone.types.glue_connection_input

        out["glue_connection_input"] = (
            aws_sdk_datazone.types.glue_connection_input.deserialize_json(
                data["glueConnectionInput"]
            )
        )
    return out
