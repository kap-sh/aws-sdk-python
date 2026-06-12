"""Generated from Smithy shape ``com.amazonaws.connect#RequiredFieldInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.task_template_field_identifier


class RequiredFieldInfo(TypedDict):
    id: NotRequired[
        "aws_sdk_connect.types.task_template_field_identifier.TaskTemplateFieldIdentifier"
    ]
    """<p>The unique identifier for the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequiredFieldInfo) -> dict:
    out: dict = {}
    if "id" in value:
        import aws_sdk_connect.types.task_template_field_identifier

        out["Id"] = aws_sdk_connect.types.task_template_field_identifier.serialize_json(
            value["id"]
        )
    return out


def deserialize_json(data: dict) -> RequiredFieldInfo:
    out: RequiredFieldInfo = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        import aws_sdk_connect.types.task_template_field_identifier

        out["id"] = (
            aws_sdk_connect.types.task_template_field_identifier.deserialize_json(
                data["Id"]
            )
        )
    return out
