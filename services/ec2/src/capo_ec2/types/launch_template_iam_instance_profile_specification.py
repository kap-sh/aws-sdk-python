"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateIamInstanceProfileSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class LaunchTemplateIamInstanceProfileSpecification(TypedDict, closed=True):
    arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the instance profile.</p>"""
    name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the instance profile.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateIamInstanceProfileSpecification,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))


def deserialize_ec2_query(el: Element) -> LaunchTemplateIamInstanceProfileSpecification:
    out: LaunchTemplateIamInstanceProfileSpecification = {}  # type: ignore[typeddict-item]
    child_arn = el.find("arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_name = el.find("name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
