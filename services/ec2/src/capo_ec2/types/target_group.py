"""Generated from Smithy shape ``com.amazonaws.ec2#TargetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class TargetGroup(TypedDict, closed=True):
    arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TargetGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))


def deserialize_ec2_query(el: Element) -> TargetGroup:
    out: TargetGroup = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
