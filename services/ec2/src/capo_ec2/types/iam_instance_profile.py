"""Generated from Smithy shape ``com.amazonaws.ec2#IamInstanceProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class IamInstanceProfile(TypedDict, closed=True):
    arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the instance profile.</p>"""
    id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance profile.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IamInstanceProfile, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "id" in value:
        pairs.append((f"{key_prefix}Id", str(value["id"])))


def deserialize_ec2_query(el: Element) -> IamInstanceProfile:
    out: IamInstanceProfile = {}  # type: ignore[typeddict-item]
    child_arn = el.find("arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_id = el.find("id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    return out
