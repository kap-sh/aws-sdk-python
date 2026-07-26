"""Generated from Smithy shape ``com.amazonaws.lakeformation#WriteOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.add_object_input
    import capo_lakeformation.types.delete_object_input


class WriteOperation(TypedDict, closed=True):
    add_object: NotRequired["capo_lakeformation.types.add_object_input.AddObjectInput"]
    """<p>A new object to add to the governed table.</p>"""
    delete_object: NotRequired[
        "capo_lakeformation.types.delete_object_input.DeleteObjectInput"
    ]
    """<p>An object to delete from the governed table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WriteOperation) -> dict:
    out: dict = {}
    if "add_object" in value:
        import capo_lakeformation.types.add_object_input

        out["AddObject"] = capo_lakeformation.types.add_object_input.serialize_json(
            value["add_object"]
        )
    if "delete_object" in value:
        import capo_lakeformation.types.delete_object_input

        out["DeleteObject"] = (
            capo_lakeformation.types.delete_object_input.serialize_json(
                value["delete_object"]
            )
        )
    return out


def deserialize_json(data: dict) -> WriteOperation:
    out: WriteOperation = {}  # type: ignore[typeddict-item]
    if "AddObject" in data:
        import capo_lakeformation.types.add_object_input

        out["add_object"] = capo_lakeformation.types.add_object_input.deserialize_json(
            data["AddObject"]
        )
    if "DeleteObject" in data:
        import capo_lakeformation.types.delete_object_input

        out["delete_object"] = (
            capo_lakeformation.types.delete_object_input.deserialize_json(
                data["DeleteObject"]
            )
        )
    return out
