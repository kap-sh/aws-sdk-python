"""Generated from Smithy shape ``com.amazonaws.eks#AccessScope``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.access_scope_type
    import aws_sdk_eks.types.string_list


class AccessScope(TypedDict):
    type: NotRequired["aws_sdk_eks.types.access_scope_type.AccessScopeType"]
    """<p>The scope type of an access policy.</p>"""
    namespaces: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>A Kubernetes <code>namespace</code> that an access policy is scoped to. A value is required if you specified <code>namespace</code> for <code>Type</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessScope) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_eks.types.access_scope_type

        out["type"] = aws_sdk_eks.types.access_scope_type.serialize_json(value["type"])
    if "namespaces" in value:
        import aws_sdk_eks.types.string_list

        out["namespaces"] = aws_sdk_eks.types.string_list.serialize_json(
            value["namespaces"]
        )
    return out


def deserialize_json(data: dict) -> AccessScope:
    out: AccessScope = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_eks.types.access_scope_type

        out["type"] = aws_sdk_eks.types.access_scope_type.deserialize_json(data["type"])
    if "namespaces" in data:
        import aws_sdk_eks.types.string_list

        out["namespaces"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["namespaces"]
        )
    return out
