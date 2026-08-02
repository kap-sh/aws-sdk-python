"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceIamInstanceProfileAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.iam_instance_profile_association_id
    import capo_ec2.types.iam_instance_profile_specification


class ReplaceIamInstanceProfileAssociationRequest(TypedDict, closed=True):
    iam_instance_profile: NotRequired[
        "capo_ec2.types.iam_instance_profile_specification.IamInstanceProfileSpecification"
    ]
    """<p>The IAM instance profile.</p>"""
    association_id: NotRequired[
        "capo_ec2.types.iam_instance_profile_association_id.IamInstanceProfileAssociationId"
    ]
    """<p>The ID of the existing IAM instance profile association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceIamInstanceProfileAssociationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "iam_instance_profile" in value:
        import capo_ec2.types.iam_instance_profile_specification

        capo_ec2.types.iam_instance_profile_specification.serialize_ec2_query(
            value["iam_instance_profile"], pairs, f"{key_prefix}IamInstanceProfile"
        )
    if "association_id" in value:
        pairs.append((f"{key_prefix}AssociationId", str(value["association_id"])))


def deserialize_ec2_query(el: Element) -> ReplaceIamInstanceProfileAssociationRequest:
    out: ReplaceIamInstanceProfileAssociationRequest = {}  # type: ignore[typeddict-item]
    child_iam_instance_profile = el.find("IamInstanceProfile")
    if child_iam_instance_profile is not None:
        import capo_ec2.types.iam_instance_profile_specification

        out["iam_instance_profile"] = (
            capo_ec2.types.iam_instance_profile_specification.deserialize_ec2_query(
                child_iam_instance_profile
            )
        )
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    return out
