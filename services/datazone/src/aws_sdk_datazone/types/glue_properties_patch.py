"""Generated from Smithy shape ``com.amazonaws.datazone#GluePropertiesPatch``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.glue_connection_patch


class GluePropertiesPatch(TypedDict):
    glue_connection_input: NotRequired[
        "aws_sdk_datazone.types.glue_connection_patch.GlueConnectionPatch"
    ]
    """<p>The Amazon Web Services Glue properties patch of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GluePropertiesPatch) -> dict:
    out: dict = {}
    if "glue_connection_input" in value:
        import aws_sdk_datazone.types.glue_connection_patch

        out["glueConnectionInput"] = (
            aws_sdk_datazone.types.glue_connection_patch.serialize_json(
                value["glue_connection_input"]
            )
        )
    return out


def deserialize_json(data: dict) -> GluePropertiesPatch:
    out: GluePropertiesPatch = {}  # type: ignore[typeddict-item]
    if "glueConnectionInput" in data:
        import aws_sdk_datazone.types.glue_connection_patch

        out["glue_connection_input"] = (
            aws_sdk_datazone.types.glue_connection_patch.deserialize_json(
                data["glueConnectionInput"]
            )
        )
    return out
