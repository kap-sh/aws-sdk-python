"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeListenerAttributesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.listener_attributes


class DescribeListenerAttributesOutput(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_elastic_load_balancing_v2.types.listener_attributes.ListenerAttributes"
    ]
    """<p>Information about the listener attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeListenerAttributesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attributes" in value:
        import capo_elastic_load_balancing_v2.types.listener_attributes

        capo_elastic_load_balancing_v2.types.listener_attributes.serialize_query(
            value["attributes"], pairs, f"{prefix}.Attributes"
        )


def deserialize_query(el: Element) -> DescribeListenerAttributesOutput:
    out: DescribeListenerAttributesOutput = {}  # type: ignore[typeddict-item]
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import capo_elastic_load_balancing_v2.types.listener_attributes

        out["attributes"] = (
            capo_elastic_load_balancing_v2.types.listener_attributes.deserialize_query(
                child_attributes
            )
        )
    return out
