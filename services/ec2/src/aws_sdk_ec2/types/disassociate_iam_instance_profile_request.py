"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateIamInstanceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.iam_instance_profile_association_id


class DisassociateIamInstanceProfileRequest(TypedDict, closed=True):
    association_id: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile_association_id.IamInstanceProfileAssociationId"
    ]
    """<p>The ID of the IAM instance profile association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateIamInstanceProfileRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))


def deserialize_ec2_query(el: Element) -> DisassociateIamInstanceProfileRequest:
    out: DisassociateIamInstanceProfileRequest = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    return out
