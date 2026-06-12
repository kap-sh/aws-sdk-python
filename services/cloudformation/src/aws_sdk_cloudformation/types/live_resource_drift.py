"""Generated from Smithy shape ``com.amazonaws.cloudformation#LiveResourceDrift``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.resource_drift_actual_value
    import aws_sdk_cloudformation.types.resource_drift_previous_value
    import aws_sdk_cloudformation.types.timestamp


class LiveResourceDrift(TypedDict):
    previous_value: NotRequired[
        "aws_sdk_cloudformation.types.resource_drift_previous_value.ResourceDriftPreviousValue"
    ]
    """<p>The configuration value from the previous CloudFormation deployment.</p>"""
    actual_value: NotRequired[
        "aws_sdk_cloudformation.types.resource_drift_actual_value.ResourceDriftActualValue"
    ]
    """<p>The current live configuration value of the resource property.</p>"""
    drift_detection_timestamp: NotRequired[
        "aws_sdk_cloudformation.types.timestamp.Timestamp"
    ]
    """<p>The timestamp when drift was detected for this resource property.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LiveResourceDrift, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "previous_value" in value:
        pairs.append((f"{prefix}.PreviousValue", str(value["previous_value"])))
    if "actual_value" in value:
        pairs.append((f"{prefix}.ActualValue", str(value["actual_value"])))
    if "drift_detection_timestamp" in value:
        import aws_sdk_cloudformation.types.timestamp

        aws_sdk_cloudformation.types.timestamp.serialize_query(
            value["drift_detection_timestamp"],
            pairs,
            f"{prefix}.DriftDetectionTimestamp",
        )


def deserialize_query(el: Element) -> LiveResourceDrift:
    out: LiveResourceDrift = {}  # type: ignore[typeddict-item]
    child_previous_value = el.find("PreviousValue")
    if child_previous_value is not None:
        out["previous_value"] = str(child_previous_value.text or "")
    child_actual_value = el.find("ActualValue")
    if child_actual_value is not None:
        out["actual_value"] = str(child_actual_value.text or "")
    child_drift_detection_timestamp = el.find("DriftDetectionTimestamp")
    if child_drift_detection_timestamp is not None:
        import aws_sdk_cloudformation.types.timestamp

        out["drift_detection_timestamp"] = (
            aws_sdk_cloudformation.types.timestamp.deserialize_query(
                child_drift_detection_timestamp
            )
        )
    return out
