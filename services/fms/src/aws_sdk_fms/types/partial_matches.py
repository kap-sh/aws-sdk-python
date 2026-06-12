"""Generated from Smithy shape ``com.amazonaws.fms#PartialMatches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.partial_match

PartialMatches: TypeAlias = list["aws_sdk_fms.types.partial_match.PartialMatch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartialMatches) -> list:
    import aws_sdk_fms.types.partial_match

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.partial_match.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PartialMatches:
    import aws_sdk_fms.types.partial_match

    out: PartialMatches = []
    for item in data:
        out.append(aws_sdk_fms.types.partial_match.deserialize_aws_json_1_1(item))
    return out
