"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateIamInstanceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.iam_instance_profile_specification
    import capo_ec2.types.instance_id


class AssociateIamInstanceProfileRequest(TypedDict, closed=True):
    iam_instance_profile: NotRequired[
        "capo_ec2.types.iam_instance_profile_specification.IamInstanceProfileSpecification"
    ]
    """<p>The IAM instance profile.</p>"""
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateIamInstanceProfileRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "iam_instance_profile" in value:
        import capo_ec2.types.iam_instance_profile_specification

        capo_ec2.types.iam_instance_profile_specification.serialize_ec2_query(
            value["iam_instance_profile"], pairs, f"{key_prefix}IamInstanceProfile"
        )
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))


def deserialize_ec2_query(el: Element) -> AssociateIamInstanceProfileRequest:
    out: AssociateIamInstanceProfileRequest = {}  # type: ignore[typeddict-item]
    child_iam_instance_profile = el.find("IamInstanceProfile")
    if child_iam_instance_profile is not None:
        import capo_ec2.types.iam_instance_profile_specification

        out["iam_instance_profile"] = (
            capo_ec2.types.iam_instance_profile_specification.deserialize_ec2_query(
                child_iam_instance_profile
            )
        )
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    return out
