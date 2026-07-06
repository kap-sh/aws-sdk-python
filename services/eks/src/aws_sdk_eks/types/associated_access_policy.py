"""Generated from Smithy shape ``com.amazonaws.eks#AssociatedAccessPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.access_scope
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.timestamp


class AssociatedAccessPolicy(TypedDict, closed=True):
    policy_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The ARN of the <code>AccessPolicy</code>.</p>"""
    access_scope: NotRequired["aws_sdk_eks.types.access_scope.AccessScope"]
    """<p>The scope of the access policy.</p>"""
    associated_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The date and time the <code>AccessPolicy</code> was associated with an <code>AccessEntry</code>.</p>"""
    modified_at: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp for the last modification to the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedAccessPolicy) -> dict:
    out: dict = {}
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "access_scope" in value:
        import aws_sdk_eks.types.access_scope

        out["accessScope"] = aws_sdk_eks.types.access_scope.serialize_json(
            value["access_scope"]
        )
    if "associated_at" in value:
        import aws_sdk_eks.types.timestamp

        out["associatedAt"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["associated_at"]
        )
    if "modified_at" in value:
        import aws_sdk_eks.types.timestamp

        out["modifiedAt"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["modified_at"]
        )
    return out


def deserialize_json(data: dict) -> AssociatedAccessPolicy:
    out: AssociatedAccessPolicy = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "accessScope" in data:
        import aws_sdk_eks.types.access_scope

        out["access_scope"] = aws_sdk_eks.types.access_scope.deserialize_json(
            data["accessScope"]
        )
    if "associatedAt" in data:
        import aws_sdk_eks.types.timestamp

        out["associated_at"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["associatedAt"]
        )
    if "modifiedAt" in data:
        import aws_sdk_eks.types.timestamp

        out["modified_at"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    return out
