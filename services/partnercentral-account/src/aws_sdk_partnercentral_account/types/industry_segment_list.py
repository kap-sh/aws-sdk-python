"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#IndustrySegmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.industry_segment

IndustrySegmentList: TypeAlias = list[
    "aws_sdk_partnercentral_account.types.industry_segment.IndustrySegment"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IndustrySegmentList) -> list:
    import aws_sdk_partnercentral_account.types.industry_segment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_account.types.industry_segment.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IndustrySegmentList:
    import aws_sdk_partnercentral_account.types.industry_segment

    out: IndustrySegmentList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_account.types.industry_segment.deserialize_aws_json_1_0(
                item
            )
        )
    return out
