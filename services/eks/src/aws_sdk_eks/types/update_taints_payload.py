"""Generated from Smithy shape ``com.amazonaws.eks#UpdateTaintsPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.taints_list


class UpdateTaintsPayload(TypedDict, closed=True):
    add_or_update_taints: NotRequired["aws_sdk_eks.types.taints_list.taintsList"]
    """<p>Kubernetes taints to be added or updated.</p>"""
    remove_taints: NotRequired["aws_sdk_eks.types.taints_list.taintsList"]
    """<p>Kubernetes taints to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTaintsPayload) -> dict:
    out: dict = {}
    if "add_or_update_taints" in value:
        import aws_sdk_eks.types.taints_list

        out["addOrUpdateTaints"] = aws_sdk_eks.types.taints_list.serialize_json(
            value["add_or_update_taints"]
        )
    if "remove_taints" in value:
        import aws_sdk_eks.types.taints_list

        out["removeTaints"] = aws_sdk_eks.types.taints_list.serialize_json(
            value["remove_taints"]
        )
    return out


def deserialize_json(data: dict) -> UpdateTaintsPayload:
    out: UpdateTaintsPayload = {}  # type: ignore[typeddict-item]
    if "addOrUpdateTaints" in data:
        import aws_sdk_eks.types.taints_list

        out["add_or_update_taints"] = aws_sdk_eks.types.taints_list.deserialize_json(
            data["addOrUpdateTaints"]
        )
    if "removeTaints" in data:
        import aws_sdk_eks.types.taints_list

        out["remove_taints"] = aws_sdk_eks.types.taints_list.deserialize_json(
            data["removeTaints"]
        )
    return out
