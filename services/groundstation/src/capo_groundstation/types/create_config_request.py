"""Generated from Smithy shape ``com.amazonaws.groundstation#CreateConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.config_type_data
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.tags_map


class CreateConfigRequest(TypedDict, closed=True):
    name: "capo_groundstation.types.safe_name.SafeName"
    """<p>Name of a <code>Config</code>.</p>"""
    config_data: "capo_groundstation.types.config_type_data.ConfigTypeData"
    """<p>Parameters of a <code>Config</code>.</p>"""
    tags: NotRequired["capo_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to a <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_groundstation.types.config_type_data

    out["configData"] = capo_groundstation.types.config_type_data.serialize_json(
        value["config_data"]
    )
    if "tags" in value:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConfigRequest:
    out: CreateConfigRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateConfigRequest.name required")
    if "configData" in data:
        import capo_groundstation.types.config_type_data

        out["config_data"] = capo_groundstation.types.config_type_data.deserialize_json(
            data["configData"]
        )
    else:
        raise DeserializationError("CreateConfigRequest.config_data required")
    if "tags" in data:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.deserialize_json(data["tags"])
    return out
