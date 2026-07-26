"""Generated from Smithy shape ``com.amazonaws.xray#Annotations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.annotation_key
    import capo_xray.types.values_with_service_ids

Annotations: TypeAlias = dict[
    "capo_xray.types.annotation_key.AnnotationKey",
    "capo_xray.types.values_with_service_ids.ValuesWithServiceIds",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Annotations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_xray.types.values_with_service_ids

        out[key] = capo_xray.types.values_with_service_ids.serialize_json(value)
    return out


def deserialize_json(data: dict) -> Annotations:
    out: Annotations = {}
    for key, value in data.items():
        import capo_xray.types.values_with_service_ids

        out[key] = capo_xray.types.values_with_service_ids.deserialize_json(value)
    return out
