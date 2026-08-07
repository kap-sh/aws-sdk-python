"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyListenerAttributesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.listener_attributes


class ModifyListenerAttributesOutput(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_elastic_load_balancing_v2.types.listener_attributes.ListenerAttributes"
    ]
    """<p>Information about the listener attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyListenerAttributesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attributes" in value:
        import capo_elastic_load_balancing_v2.types.listener_attributes

        capo_elastic_load_balancing_v2.types.listener_attributes.serialize_query(
            value["attributes"], pairs, f"{key_prefix}Attributes"
        )


def deserialize_query(el: Element) -> ModifyListenerAttributesOutput:
    out: ModifyListenerAttributesOutput = {}  # type: ignore[typeddict-item]
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import capo_elastic_load_balancing_v2.types.listener_attributes

        out["attributes"] = (
            capo_elastic_load_balancing_v2.types.listener_attributes.deserialize_query(
                child_attributes
            )
        )
    return out
