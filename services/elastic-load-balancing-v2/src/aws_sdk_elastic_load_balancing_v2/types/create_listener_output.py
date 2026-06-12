"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CreateListenerOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.listeners


class CreateListenerOutput(TypedDict):
    listeners: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.listeners.Listeners"
    ]
    """<p>Information about the listener.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateListenerOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "listeners" in value:
        import aws_sdk_elastic_load_balancing_v2.types.listeners

        aws_sdk_elastic_load_balancing_v2.types.listeners.serialize_query(
            value["listeners"], pairs, f"{prefix}.Listeners"
        )


def deserialize_query(el: Element) -> CreateListenerOutput:
    out: CreateListenerOutput = {}  # type: ignore[typeddict-item]
    child_listeners = el.find("Listeners")
    if child_listeners is not None:
        import aws_sdk_elastic_load_balancing_v2.types.listeners

        out["listeners"] = (
            aws_sdk_elastic_load_balancing_v2.types.listeners.deserialize_query(
                child_listeners
            )
        )
    return out
