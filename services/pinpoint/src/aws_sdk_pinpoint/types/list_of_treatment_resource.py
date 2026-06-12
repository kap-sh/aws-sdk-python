"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfTreatmentResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.treatment_resource

ListOfTreatmentResource: TypeAlias = list[
    "aws_sdk_pinpoint.types.treatment_resource.TreatmentResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfTreatmentResource) -> list:
    import aws_sdk_pinpoint.types.treatment_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.treatment_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfTreatmentResource:
    import aws_sdk_pinpoint.types.treatment_resource

    out: ListOfTreatmentResource = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.treatment_resource.deserialize_json(item))
    return out
