"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentOrder``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.string


class ServiceEnvironmentOrder(TypedDict):
    order: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The order of the service environment. Job queues with a higher priority are evaluated first when associated with the same service environment.</p>"""
    service_environment: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name or ARN of the service environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEnvironmentOrder) -> dict:
    out: dict = {}
    if "order" in value:
        out["order"] = value["order"]
    if "service_environment" in value:
        out["serviceEnvironment"] = value["service_environment"]
    return out


def deserialize_json(data: dict) -> ServiceEnvironmentOrder:
    out: ServiceEnvironmentOrder = {}  # type: ignore[typeddict-item]
    if "order" in data:
        out["order"] = data["order"]
    if "serviceEnvironment" in data:
        out["service_environment"] = data["serviceEnvironment"]
    return out
