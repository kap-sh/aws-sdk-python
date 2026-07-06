"""Generated from Smithy shape ``com.amazonaws.quicksight#MemberIdArnPair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.restrictive_resource_id


class MemberIdArnPair(TypedDict, closed=True):
    member_id: NotRequired[
        "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    ]
    """<p>The ID of the member.</p>"""
    member_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberIdArnPair) -> dict:
    out: dict = {}
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    if "member_arn" in value:
        out["MemberArn"] = value["member_arn"]
    return out


def deserialize_json(data: dict) -> MemberIdArnPair:
    out: MemberIdArnPair = {}  # type: ignore[typeddict-item]
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    if "MemberArn" in data:
        out["member_arn"] = data["MemberArn"]
    return out
