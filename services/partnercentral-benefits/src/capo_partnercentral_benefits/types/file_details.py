"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#FileDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.file_detail

FileDetails: TypeAlias = list[
    "capo_partnercentral_benefits.types.file_detail.FileDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FileDetails) -> list:
    import capo_partnercentral_benefits.types.file_detail

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_benefits.types.file_detail.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FileDetails:
    import capo_partnercentral_benefits.types.file_detail

    out: FileDetails = []
    for item in data:
        out.append(
            capo_partnercentral_benefits.types.file_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out
