"""Generated from Smithy shape ``com.amazonaws.connect#ReadOnlyFieldInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.task_template_field_identifier


class ReadOnlyFieldInfo(TypedDict, closed=True):
    id: NotRequired[
        "capo_connect.types.task_template_field_identifier.TaskTemplateFieldIdentifier"
    ]
    """<p>Identifier of the read-only field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadOnlyFieldInfo) -> dict:
    out: dict = {}
    if "id" in value:
        import capo_connect.types.task_template_field_identifier

        out["Id"] = capo_connect.types.task_template_field_identifier.serialize_json(
            value["id"]
        )
    return out


def deserialize_json(data: dict) -> ReadOnlyFieldInfo:
    out: ReadOnlyFieldInfo = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        import capo_connect.types.task_template_field_identifier

        out["id"] = capo_connect.types.task_template_field_identifier.deserialize_json(
            data["Id"]
        )
    return out
