"""Generated from Smithy shape ``com.amazonaws.shield#DescribeAttackResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_shield.types.attack_detail


class DescribeAttackResponse(TypedDict):
    attack: NotRequired["aws_sdk_shield.types.attack_detail.AttackDetail"]
    """<p>The attack that you requested. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAttackResponse) -> dict:
    out: dict = {}
    if "attack" in value:
        import aws_sdk_shield.types.attack_detail

        out["Attack"] = aws_sdk_shield.types.attack_detail.serialize_aws_json_1_1(
            value["attack"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAttackResponse:
    out: DescribeAttackResponse = {}  # type: ignore[typeddict-item]
    if "Attack" in data:
        import aws_sdk_shield.types.attack_detail

        out["attack"] = aws_sdk_shield.types.attack_detail.deserialize_aws_json_1_1(
            data["Attack"]
        )
    return out
