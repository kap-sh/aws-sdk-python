"""Generated from Smithy shape ``com.amazonaws.ec2#IamInstanceProfileAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.iam_instance_profile
    import capo_ec2.types.iam_instance_profile_association_state
    import capo_ec2.types.string


class IamInstanceProfileAssociation(TypedDict, closed=True):
    association_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the association.</p>"""
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    iam_instance_profile: NotRequired[
        "capo_ec2.types.iam_instance_profile.IamInstanceProfile"
    ]
    """<p>The IAM instance profile.</p>"""
    state: NotRequired[
        "capo_ec2.types.iam_instance_profile_association_state.IamInstanceProfileAssociationState"
    ]
    """<p>The state of the association.</p>"""
    timestamp: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time the IAM instance profile was associated with the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IamInstanceProfileAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "association_id" in value:
        pairs.append((f"{key_prefix}AssociationId", str(value["association_id"])))
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "iam_instance_profile" in value:
        import capo_ec2.types.iam_instance_profile

        capo_ec2.types.iam_instance_profile.serialize_ec2_query(
            value["iam_instance_profile"], pairs, f"{key_prefix}IamInstanceProfile"
        )
    if "state" in value:
        import capo_ec2.types.iam_instance_profile_association_state

        capo_ec2.types.iam_instance_profile_association_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "timestamp" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
        )


def deserialize_ec2_query(el: Element) -> IamInstanceProfileAssociation:
    out: IamInstanceProfileAssociation = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_iam_instance_profile = el.find("IamInstanceProfile")
    if child_iam_instance_profile is not None:
        import capo_ec2.types.iam_instance_profile

        out["iam_instance_profile"] = (
            capo_ec2.types.iam_instance_profile.deserialize_ec2_query(
                child_iam_instance_profile
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.iam_instance_profile_association_state

        out["state"] = (
            capo_ec2.types.iam_instance_profile_association_state.deserialize_ec2_query(
                child_state
            )
        )
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import capo_ec2.types.date_time

        out["timestamp"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_timestamp
        )
    return out
