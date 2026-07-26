"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttachPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.object_reference


class AttachPolicyRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where both objects reside. For more information, see <a>arns</a>.</p>"""
    policy_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>The reference that is associated with the policy object.</p>"""
    object_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>The reference that identifies the object to which the policy will be attached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachPolicyRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.object_reference

    out["PolicyReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["policy_reference"]
    )
    import capo_clouddirectory.types.object_reference

    out["ObjectReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["object_reference"]
    )
    return out


def deserialize_json(data: dict) -> AttachPolicyRequest:
    out: AttachPolicyRequest = {}  # type: ignore[typeddict-item]
    if "PolicyReference" in data:
        import capo_clouddirectory.types.object_reference

        out["policy_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["PolicyReference"]
            )
        )
    else:
        raise DeserializationError("AttachPolicyRequest.policy_reference required")
    if "ObjectReference" in data:
        import capo_clouddirectory.types.object_reference

        out["object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("AttachPolicyRequest.object_reference required")
    return out
