"""Generated from Smithy shape ``com.amazonaws.costexplorer#Group``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.keys
    import capo_cost_explorer.types.metrics


class Group(TypedDict, closed=True):
    keys: NotRequired["capo_cost_explorer.types.keys.Keys"]
    """<p>The keys that are included in this group.</p>"""
    metrics: NotRequired["capo_cost_explorer.types.metrics.Metrics"]
    """<p>The metrics that are included in this group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Group) -> dict:
    out: dict = {}
    if "keys" in value:
        import capo_cost_explorer.types.keys

        out["Keys"] = capo_cost_explorer.types.keys.serialize_aws_json_1_1(
            value["keys"]
        )
    if "metrics" in value:
        import capo_cost_explorer.types.metrics

        out["Metrics"] = capo_cost_explorer.types.metrics.serialize_aws_json_1_1(
            value["metrics"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    if "Keys" in data:
        import capo_cost_explorer.types.keys

        out["keys"] = capo_cost_explorer.types.keys.deserialize_aws_json_1_1(
            data["Keys"]
        )
    if "Metrics" in data:
        import capo_cost_explorer.types.metrics

        out["metrics"] = capo_cost_explorer.types.metrics.deserialize_aws_json_1_1(
            data["Metrics"]
        )
    return out
