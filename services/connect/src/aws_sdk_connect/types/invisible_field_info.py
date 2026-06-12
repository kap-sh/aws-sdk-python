"""Generated from Smithy shape ``com.amazonaws.connect#InvisibleFieldInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.task_template_field_identifier


class InvisibleFieldInfo(TypedDict):
    id: NotRequired[
        "aws_sdk_connect.types.task_template_field_identifier.TaskTemplateFieldIdentifier"
    ]
    """<p>Identifier of the invisible field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvisibleFieldInfo) -> dict:
    out: dict = {}
    if "id" in value:
        import aws_sdk_connect.types.task_template_field_identifier

        out["Id"] = aws_sdk_connect.types.task_template_field_identifier.serialize_json(
            value["id"]
        )
    return out


def deserialize_json(data: dict) -> InvisibleFieldInfo:
    out: InvisibleFieldInfo = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        import aws_sdk_connect.types.task_template_field_identifier

        out["id"] = (
            aws_sdk_connect.types.task_template_field_identifier.deserialize_json(
                data["Id"]
            )
        )
    return out
