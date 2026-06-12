"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#Target``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn


class Target(TypedDict):
    member_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the target channel member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Target) -> dict:
    out: dict = {}
    if "member_arn" in value:
        out["MemberArn"] = value["member_arn"]
    return out


def deserialize_json(data: dict) -> Target:
    out: Target = {}  # type: ignore[typeddict-item]
    if "MemberArn" in data:
        out["member_arn"] = data["MemberArn"]
    return out
