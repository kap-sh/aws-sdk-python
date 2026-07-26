"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfTreatmentResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.treatment_resource

ListOfTreatmentResource: TypeAlias = list[
    "capo_pinpoint.types.treatment_resource.TreatmentResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfTreatmentResource) -> list:
    import capo_pinpoint.types.treatment_resource

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.treatment_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfTreatmentResource:
    import capo_pinpoint.types.treatment_resource

    out: ListOfTreatmentResource = []
    for item in data:
        out.append(capo_pinpoint.types.treatment_resource.deserialize_json(item))
    return out
