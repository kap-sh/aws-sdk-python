"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesIamInstanceProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ScheduledInstancesIamInstanceProfile(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN).</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstancesIamInstanceProfile,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))


def deserialize_ec2_query(el: Element) -> ScheduledInstancesIamInstanceProfile:
    out: ScheduledInstancesIamInstanceProfile = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
