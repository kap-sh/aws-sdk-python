"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceOperationEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_entity


class ServiceOperationEntity(TypedDict, closed=True):
    service: NotRequired[
        "aws_sdk_application_signals.types.service_entity.ServiceEntity"
    ]
    """<p>The service entity that contains this operation.</p>"""
    operation: NotRequired["str"]
    """<p>The name of the operation.</p>"""
    metric_type: NotRequired["str"]
    """<p>The type of metric associated with this service operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceOperationEntity) -> dict:
    out: dict = {}
    if "service" in value:
        import aws_sdk_application_signals.types.service_entity

        out["Service"] = (
            aws_sdk_application_signals.types.service_entity.serialize_json(
                value["service"]
            )
        )
    if "operation" in value:
        out["Operation"] = value["operation"]
    if "metric_type" in value:
        out["MetricType"] = value["metric_type"]
    return out


def deserialize_json(data: dict) -> ServiceOperationEntity:
    out: ServiceOperationEntity = {}  # type: ignore[typeddict-item]
    if "Service" in data:
        import aws_sdk_application_signals.types.service_entity

        out["service"] = (
            aws_sdk_application_signals.types.service_entity.deserialize_json(
                data["Service"]
            )
        )
    if "Operation" in data:
        out["operation"] = data["Operation"]
    if "MetricType" in data:
        out["metric_type"] = data["MetricType"]
    return out
