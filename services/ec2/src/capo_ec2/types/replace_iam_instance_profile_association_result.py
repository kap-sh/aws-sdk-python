"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceIamInstanceProfileAssociationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.iam_instance_profile_association


class ReplaceIamInstanceProfileAssociationResult(TypedDict, closed=True):
    iam_instance_profile_association: NotRequired[
        "capo_ec2.types.iam_instance_profile_association.IamInstanceProfileAssociation"
    ]
    """<p>Information about the IAM instance profile association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceIamInstanceProfileAssociationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "iam_instance_profile_association" in value:
        import capo_ec2.types.iam_instance_profile_association

        capo_ec2.types.iam_instance_profile_association.serialize_ec2_query(
            value["iam_instance_profile_association"],
            pairs,
            f"{key_prefix}IamInstanceProfileAssociation",
        )


def deserialize_ec2_query(el: Element) -> ReplaceIamInstanceProfileAssociationResult:
    out: ReplaceIamInstanceProfileAssociationResult = {}  # type: ignore[typeddict-item]
    child_iam_instance_profile_association = el.find("IamInstanceProfileAssociation")
    if child_iam_instance_profile_association is not None:
        import capo_ec2.types.iam_instance_profile_association

        out["iam_instance_profile_association"] = (
            capo_ec2.types.iam_instance_profile_association.deserialize_ec2_query(
                child_iam_instance_profile_association
            )
        )
    return out
