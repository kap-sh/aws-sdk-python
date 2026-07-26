"""Generated from Smithy shape ``com.amazonaws.groundstation#ComponentVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.component_type_string
    import capo_groundstation.types.version_string_list


class ComponentVersion(TypedDict, closed=True):
    component_type: "capo_groundstation.types.component_type_string.ComponentTypeString"
    """<p>Component type.</p>"""
    versions: "capo_groundstation.types.version_string_list.VersionStringList"
    """<p>List of versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentVersion) -> dict:
    out: dict = {}
    out["componentType"] = value["component_type"]
    import capo_groundstation.types.version_string_list

    out["versions"] = capo_groundstation.types.version_string_list.serialize_json(
        value["versions"]
    )
    return out


def deserialize_json(data: dict) -> ComponentVersion:
    out: ComponentVersion = {}  # type: ignore[typeddict-item]
    if "componentType" in data:
        out["component_type"] = data["componentType"]
    else:
        raise DeserializationError("ComponentVersion.component_type required")
    if "versions" in data:
        import capo_groundstation.types.version_string_list

        out["versions"] = capo_groundstation.types.version_string_list.deserialize_json(
            data["versions"]
        )
    else:
        raise DeserializationError("ComponentVersion.versions required")
    return out
