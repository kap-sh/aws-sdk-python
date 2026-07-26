"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationRunTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.metadata_generation_target_type
    import capo_datazone.types.revision


class MetadataGenerationRunTarget(TypedDict, closed=True):
    type: "capo_datazone.types.metadata_generation_target_type.MetadataGenerationTargetType"
    """<p>The type of the asset for which metadata was generated.</p>"""
    identifier: "str"
    """<p>The ID of the metadata generation run's target.</p>"""
    revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the asset for which metadata was generated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataGenerationRunTarget) -> dict:
    out: dict = {}
    import capo_datazone.types.metadata_generation_target_type

    out["type"] = capo_datazone.types.metadata_generation_target_type.serialize_json(
        value["type"]
    )
    out["identifier"] = value["identifier"]
    if "revision" in value:
        out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> MetadataGenerationRunTarget:
    out: MetadataGenerationRunTarget = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_datazone.types.metadata_generation_target_type

        out["type"] = (
            capo_datazone.types.metadata_generation_target_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("MetadataGenerationRunTarget.type required")
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("MetadataGenerationRunTarget.identifier required")
    if "revision" in data:
        out["revision"] = data["revision"]
    return out
