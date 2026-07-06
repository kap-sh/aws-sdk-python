"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupArbitraryPatternLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_shield.types.long


class ProtectionGroupArbitraryPatternLimits(TypedDict, closed=True):
    max_members: "aws_sdk_shield.types.long.Long"
    """<p>The maximum number of resources you can specify for a single arbitrary pattern in a protection group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroupArbitraryPatternLimits) -> dict:
    out: dict = {}
    out["MaxMembers"] = value.get("max_members", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectionGroupArbitraryPatternLimits:
    out: ProtectionGroupArbitraryPatternLimits = {}  # type: ignore[typeddict-item]
    if "MaxMembers" in data:
        out["max_members"] = data["MaxMembers"]
    else:
        out["max_members"] = 0
    return out
