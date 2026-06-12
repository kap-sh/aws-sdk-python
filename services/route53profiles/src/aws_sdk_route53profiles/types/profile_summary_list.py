"""Generated from Smithy shape ``com.amazonaws.route53profiles#ProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.profile_summary

ProfileSummaryList: TypeAlias = list[
    "aws_sdk_route53profiles.types.profile_summary.ProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileSummaryList) -> list:
    import aws_sdk_route53profiles.types.profile_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_route53profiles.types.profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileSummaryList:
    import aws_sdk_route53profiles.types.profile_summary

    out: ProfileSummaryList = []
    for item in data:
        out.append(aws_sdk_route53profiles.types.profile_summary.deserialize_json(item))
    return out
