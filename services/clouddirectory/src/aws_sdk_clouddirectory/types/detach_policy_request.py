"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DetachPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.object_reference


class DetachPolicyRequest(TypedDict):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where both objects reside. For more information, see <a>arns</a>.</p>"""
    policy_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>Reference that identifies the policy object.</p>"""
    object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>Reference that identifies the object whose policy object will be detached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetachPolicyRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["PolicyReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["policy_reference"]
        )
    )
    import aws_sdk_clouddirectory.types.object_reference

    out["ObjectReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["object_reference"]
        )
    )
    return out


def deserialize_json(data: dict) -> DetachPolicyRequest:
    out: DetachPolicyRequest = {}  # type: ignore[typeddict-item]
    if "PolicyReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["policy_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["PolicyReference"]
            )
        )
    else:
        raise DeserializationError("DetachPolicyRequest.policy_reference required")
    if "ObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("DetachPolicyRequest.object_reference required")
    return out
