"""Generated from Smithy shape ``com.amazonaws.connect#ContactMetricResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_metric_name
    import aws_sdk_connect.types.contact_metric_value


class ContactMetricResult(TypedDict):
    name: "aws_sdk_connect.types.contact_metric_name.ContactMetricName"
    """<p>The name of the metric that was retrieved. This corresponds to the metric name specified in the request, such as POSITION_IN_QUEUE or ESTIMATED_WAIT_TIME.</p>"""
    value: "aws_sdk_connect.types.contact_metric_value.ContactMetricValue"
    """<p>The calculated value for the requested metric. This object contains the numeric result based on the contact's current state in the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactMetricResult) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.contact_metric_name

    out["Name"] = aws_sdk_connect.types.contact_metric_name.serialize_json(
        value["name"]
    )
    import aws_sdk_connect.types.contact_metric_value

    out["Value"] = aws_sdk_connect.types.contact_metric_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> ContactMetricResult:
    out: ContactMetricResult = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_connect.types.contact_metric_name

        out["name"] = aws_sdk_connect.types.contact_metric_name.deserialize_json(
            data["Name"]
        )
    else:
        raise DeserializationError("ContactMetricResult.name required")
    if "Value" in data:
        import aws_sdk_connect.types.contact_metric_value

        out["value"] = aws_sdk_connect.types.contact_metric_value.deserialize_json(
            data["Value"]
        )
    else:
        raise DeserializationError("ContactMetricResult.value required")
    return out
