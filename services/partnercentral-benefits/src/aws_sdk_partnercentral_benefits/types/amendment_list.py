"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#AmendmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.amendment

AmendmentList: TypeAlias = list[
    "aws_sdk_partnercentral_benefits.types.amendment.Amendment"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AmendmentList) -> list:
    import aws_sdk_partnercentral_benefits.types.amendment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_benefits.types.amendment.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AmendmentList:
    import aws_sdk_partnercentral_benefits.types.amendment

    out: AmendmentList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_benefits.types.amendment.deserialize_aws_json_1_0(
                item
            )
        )
    return out
