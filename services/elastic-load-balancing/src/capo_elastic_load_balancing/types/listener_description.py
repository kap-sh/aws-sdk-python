"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ListenerDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.listener
    import capo_elastic_load_balancing.types.policy_names


class ListenerDescription(TypedDict, closed=True):
    listener: NotRequired["capo_elastic_load_balancing.types.listener.Listener"]
    """<p>The listener.</p>"""
    policy_names: NotRequired[
        "capo_elastic_load_balancing.types.policy_names.PolicyNames"
    ]
    """<p>The policies. If there are no policies enabled, the list is empty.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListenerDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "listener" in value:
        import capo_elastic_load_balancing.types.listener

        capo_elastic_load_balancing.types.listener.serialize_query(
            value["listener"], pairs, f"{prefix}.Listener"
        )
    if "policy_names" in value:
        import capo_elastic_load_balancing.types.policy_names

        capo_elastic_load_balancing.types.policy_names.serialize_query(
            value["policy_names"], pairs, f"{prefix}.PolicyNames"
        )


def deserialize_query(el: Element) -> ListenerDescription:
    out: ListenerDescription = {}  # type: ignore[typeddict-item]
    child_listener = el.find("Listener")
    if child_listener is not None:
        import capo_elastic_load_balancing.types.listener

        out["listener"] = capo_elastic_load_balancing.types.listener.deserialize_query(
            child_listener
        )
    child_policy_names = el.find("PolicyNames")
    if child_policy_names is not None:
        import capo_elastic_load_balancing.types.policy_names

        out["policy_names"] = (
            capo_elastic_load_balancing.types.policy_names.deserialize_query(
                child_policy_names
            )
        )
    return out
