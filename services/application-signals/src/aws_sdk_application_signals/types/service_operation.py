"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.metric_references
    import aws_sdk_application_signals.types.operation_name


class ServiceOperation(TypedDict, closed=True):
    name: "aws_sdk_application_signals.types.operation_name.OperationName"
    """<p>The name of the operation, discovered by Application Signals.</p>"""
    metric_references: (
        "aws_sdk_application_signals.types.metric_references.MetricReferences"
    )
    """<p>An array of structures that each contain information about one metric associated with this service operation that was discovered by Application Signals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceOperation) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_application_signals.types.metric_references

    out["MetricReferences"] = (
        aws_sdk_application_signals.types.metric_references.serialize_json(
            value["metric_references"]
        )
    )
    return out


def deserialize_json(data: dict) -> ServiceOperation:
    out: ServiceOperation = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ServiceOperation.name required")
    if "MetricReferences" in data:
        import aws_sdk_application_signals.types.metric_references

        out["metric_references"] = (
            aws_sdk_application_signals.types.metric_references.deserialize_json(
                data["MetricReferences"]
            )
        )
    else:
        raise DeserializationError("ServiceOperation.metric_references required")
    return out
