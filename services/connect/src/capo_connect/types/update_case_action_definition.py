"""Generated from Smithy shape ``com.amazonaws.connect#UpdateCaseActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.field_values


class UpdateCaseActionDefinition(TypedDict, closed=True):
    fields: "capo_connect.types.field_values.FieldValues"
    """<p>An array of objects with <code>Field ID</code> and Value data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCaseActionDefinition) -> dict:
    out: dict = {}
    import capo_connect.types.field_values

    out["Fields"] = capo_connect.types.field_values.serialize_json(value["fields"])
    return out


def deserialize_json(data: dict) -> UpdateCaseActionDefinition:
    out: UpdateCaseActionDefinition = {}  # type: ignore[typeddict-item]
    if "Fields" in data:
        import capo_connect.types.field_values

        out["fields"] = capo_connect.types.field_values.deserialize_json(data["Fields"])
    else:
        raise DeserializationError("UpdateCaseActionDefinition.fields required")
    return out
