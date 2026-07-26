"""Generated from Smithy shape ``com.amazonaws.medicalimaging#MetadataCopies``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.copiable_attributes


class MetadataCopies(TypedDict, closed=True):
    copiable_attributes: (
        "capo_medical_imaging.types.copiable_attributes.CopiableAttributes"
    )
    """<p>The JSON string used to specify a subset of SOP Instances to copy from source to destination image set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataCopies) -> dict:
    out: dict = {}
    out["copiableAttributes"] = value["copiable_attributes"]
    return out


def deserialize_json(data: dict) -> MetadataCopies:
    out: MetadataCopies = {}  # type: ignore[typeddict-item]
    if "copiableAttributes" in data:
        out["copiable_attributes"] = data["copiableAttributes"]
    else:
        raise DeserializationError("MetadataCopies.copiable_attributes required")
    return out
