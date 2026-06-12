"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfWriteTreatmentResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.write_treatment_resource

ListOfWriteTreatmentResource: TypeAlias = list[
    "aws_sdk_pinpoint.types.write_treatment_resource.WriteTreatmentResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfWriteTreatmentResource) -> list:
    import aws_sdk_pinpoint.types.write_treatment_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.write_treatment_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfWriteTreatmentResource:
    import aws_sdk_pinpoint.types.write_treatment_resource

    out: ListOfWriteTreatmentResource = []
    for item in data:
        out.append(
            aws_sdk_pinpoint.types.write_treatment_resource.deserialize_json(item)
        )
    return out
