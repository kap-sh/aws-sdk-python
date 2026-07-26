"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#Target``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn


class Target(TypedDict, closed=True):
    member_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
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
