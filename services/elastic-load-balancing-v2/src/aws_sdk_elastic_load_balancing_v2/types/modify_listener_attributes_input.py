"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyListenerAttributesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.listener_arn
    import aws_sdk_elastic_load_balancing_v2.types.listener_attributes


class ModifyListenerAttributesInput(TypedDict):
    listener_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    attributes: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.listener_attributes.ListenerAttributes"
    ]
    """<p>The listener attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyListenerAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "listener_arn" in value:
        pairs.append((f"{prefix}.ListenerArn", str(value["listener_arn"])))
    if "attributes" in value:
        import aws_sdk_elastic_load_balancing_v2.types.listener_attributes

        aws_sdk_elastic_load_balancing_v2.types.listener_attributes.serialize_query(
            value["attributes"], pairs, f"{prefix}.Attributes"
        )


def deserialize_query(el: Element) -> ModifyListenerAttributesInput:
    out: ModifyListenerAttributesInput = {}  # type: ignore[typeddict-item]
    child_listener_arn = el.find("ListenerArn")
    if child_listener_arn is not None:
        out["listener_arn"] = str(child_listener_arn.text or "")
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import aws_sdk_elastic_load_balancing_v2.types.listener_attributes

        out["attributes"] = (
            aws_sdk_elastic_load_balancing_v2.types.listener_attributes.deserialize_query(
                child_attributes
            )
        )
    return out
