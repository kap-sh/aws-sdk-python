"""Generated from Smithy shape ``com.amazonaws.quicksight#UserIndexCapacity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.integer_value
    import aws_sdk_quicksight.types.long_value


class UserIndexCapacity(TypedDict):
    user_arn: NotRequired["str"]
    """<p>The ARN of the user.</p>"""
    user_name: NotRequired["str"]
    """<p>The username of the user.</p>"""
    email: NotRequired["str"]
    """<p>The email address of the user.</p>"""
    role: NotRequired["str"]
    """<p>The role of the user.</p>"""
    total_capacity_bytes: NotRequired["aws_sdk_quicksight.types.long_value.LongValue"]
    """<p>The total index capacity consumed by the user in bytes.</p>"""
    total_kb_capacity_bytes: NotRequired[
        "aws_sdk_quicksight.types.long_value.LongValue"
    ]
    """<p>The total index capacity consumed by the user's knowledge bases in bytes.</p>"""
    total_space_capacity_bytes: NotRequired[
        "aws_sdk_quicksight.types.long_value.LongValue"
    ]
    """<p>The total index capacity consumed by the user's spaces in bytes.</p>"""
    kb_count: NotRequired["aws_sdk_quicksight.types.integer_value.IntegerValue"]
    """<p>The number of knowledge bases owned by the user.</p>"""
    space_count: NotRequired["aws_sdk_quicksight.types.integer_value.IntegerValue"]
    """<p>The number of spaces owned by the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserIndexCapacity) -> dict:
    out: dict = {}
    if "user_arn" in value:
        out["userArn"] = value["user_arn"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "email" in value:
        out["email"] = value["email"]
    if "role" in value:
        out["role"] = value["role"]
    if "total_capacity_bytes" in value:
        out["totalCapacityBytes"] = value["total_capacity_bytes"]
    if "total_kb_capacity_bytes" in value:
        out["totalKBCapacityBytes"] = value["total_kb_capacity_bytes"]
    if "total_space_capacity_bytes" in value:
        out["totalSpaceCapacityBytes"] = value["total_space_capacity_bytes"]
    if "kb_count" in value:
        out["kbCount"] = value["kb_count"]
    if "space_count" in value:
        out["spaceCount"] = value["space_count"]
    return out


def deserialize_json(data: dict) -> UserIndexCapacity:
    out: UserIndexCapacity = {}  # type: ignore[typeddict-item]
    if "userArn" in data:
        out["user_arn"] = data["userArn"]
    if "userName" in data:
        out["user_name"] = data["userName"]
    if "email" in data:
        out["email"] = data["email"]
    if "role" in data:
        out["role"] = data["role"]
    if "totalCapacityBytes" in data:
        out["total_capacity_bytes"] = data["totalCapacityBytes"]
    if "totalKBCapacityBytes" in data:
        out["total_kb_capacity_bytes"] = data["totalKBCapacityBytes"]
    if "totalSpaceCapacityBytes" in data:
        out["total_space_capacity_bytes"] = data["totalSpaceCapacityBytes"]
    if "kbCount" in data:
        out["kb_count"] = data["kbCount"]
    if "spaceCount" in data:
        out["space_count"] = data["spaceCount"]
    return out
