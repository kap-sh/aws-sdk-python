"""Generated from Smithy shape ``com.amazonaws.eks#UpdateLabelsPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.labels_key_list
    import capo_eks.types.labels_map


class UpdateLabelsPayload(TypedDict, closed=True):
    add_or_update_labels: NotRequired["capo_eks.types.labels_map.labelsMap"]
    """<p>The Kubernetes <code>labels</code> to add or update.</p>"""
    remove_labels: NotRequired["capo_eks.types.labels_key_list.labelsKeyList"]
    """<p>The Kubernetes <code>labels</code> to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLabelsPayload) -> dict:
    out: dict = {}
    if "add_or_update_labels" in value:
        import capo_eks.types.labels_map

        out["addOrUpdateLabels"] = capo_eks.types.labels_map.serialize_json(
            value["add_or_update_labels"]
        )
    if "remove_labels" in value:
        import capo_eks.types.labels_key_list

        out["removeLabels"] = capo_eks.types.labels_key_list.serialize_json(
            value["remove_labels"]
        )
    return out


def deserialize_json(data: dict) -> UpdateLabelsPayload:
    out: UpdateLabelsPayload = {}  # type: ignore[typeddict-item]
    if "addOrUpdateLabels" in data:
        import capo_eks.types.labels_map

        out["add_or_update_labels"] = capo_eks.types.labels_map.deserialize_json(
            data["addOrUpdateLabels"]
        )
    if "removeLabels" in data:
        import capo_eks.types.labels_key_list

        out["remove_labels"] = capo_eks.types.labels_key_list.deserialize_json(
            data["removeLabels"]
        )
    return out
