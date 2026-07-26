"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#FileInputDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.file_input

FileInputDetails: TypeAlias = list[
    "capo_partnercentral_benefits.types.file_input.FileInput"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FileInputDetails) -> list:
    import capo_partnercentral_benefits.types.file_input

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_benefits.types.file_input.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FileInputDetails:
    import capo_partnercentral_benefits.types.file_input

    out: FileInputDetails = []
    for item in data:
        out.append(
            capo_partnercentral_benefits.types.file_input.deserialize_aws_json_1_0(item)
        )
    return out
