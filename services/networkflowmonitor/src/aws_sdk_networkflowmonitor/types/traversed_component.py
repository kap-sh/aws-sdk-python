"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#TraversedComponent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.arn
    import aws_sdk_networkflowmonitor.types.component
    import aws_sdk_networkflowmonitor.types.component_type


class TraversedComponent(TypedDict):
    component_id: NotRequired["aws_sdk_networkflowmonitor.types.component.Component"]
    """<p>The identifier for the traversed component.</p>"""
    component_type: NotRequired[
        "aws_sdk_networkflowmonitor.types.component_type.ComponentType"
    ]
    """<p>The type of component that was traversed.</p>"""
    component_arn: NotRequired["aws_sdk_networkflowmonitor.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of a traversed component.</p>"""
    service_name: NotRequired["str"]
    """<p>The service name for the traversed component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TraversedComponent) -> dict:
    out: dict = {}
    if "component_id" in value:
        out["componentId"] = value["component_id"]
    if "component_type" in value:
        out["componentType"] = value["component_type"]
    if "component_arn" in value:
        out["componentArn"] = value["component_arn"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    return out


def deserialize_json(data: dict) -> TraversedComponent:
    out: TraversedComponent = {}  # type: ignore[typeddict-item]
    if "componentId" in data:
        out["component_id"] = data["componentId"]
    if "componentType" in data:
        out["component_type"] = data["componentType"]
    if "componentArn" in data:
        out["component_arn"] = data["componentArn"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    return out
