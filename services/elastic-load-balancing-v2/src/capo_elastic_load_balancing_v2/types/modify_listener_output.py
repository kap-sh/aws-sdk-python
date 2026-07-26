"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyListenerOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.listeners


class ModifyListenerOutput(TypedDict, closed=True):
    listeners: NotRequired["capo_elastic_load_balancing_v2.types.listeners.Listeners"]
    """<p>Information about the modified listener.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyListenerOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "listeners" in value:
        import capo_elastic_load_balancing_v2.types.listeners

        capo_elastic_load_balancing_v2.types.listeners.serialize_query(
            value["listeners"], pairs, f"{prefix}.Listeners"
        )


def deserialize_query(el: Element) -> ModifyListenerOutput:
    out: ModifyListenerOutput = {}  # type: ignore[typeddict-item]
    child_listeners = el.find("Listeners")
    if child_listeners is not None:
        import capo_elastic_load_balancing_v2.types.listeners

        out["listeners"] = (
            capo_elastic_load_balancing_v2.types.listeners.deserialize_query(
                child_listeners
            )
        )
    return out
