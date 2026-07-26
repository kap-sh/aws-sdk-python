"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ImportOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_neptune_graph.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_neptune_graph.types.neptune_import_options


class _ImportOptions_neptune(TypedDict, closed=True):
    neptune: "capo_neptune_graph.types.neptune_import_options.NeptuneImportOptions"


ImportOptions: TypeAlias = _ImportOptions_neptune


# --- restJson1 ser/de ---
def serialize_json(value: ImportOptions) -> dict:
    if "neptune" in value:
        import capo_neptune_graph.types.neptune_import_options

        return {
            "neptune": capo_neptune_graph.types.neptune_import_options.serialize_json(
                value["neptune"]
            )
        }
    else:
        raise SerializationError("ImportOptions: no variant present")


def deserialize_json(data: dict) -> ImportOptions:
    if "neptune" in data:
        import capo_neptune_graph.types.neptune_import_options

        return {
            "neptune": capo_neptune_graph.types.neptune_import_options.deserialize_json(
                data["neptune"]
            )
        }
    else:
        raise DeserializationError("ImportOptions: no recognized variant key")
