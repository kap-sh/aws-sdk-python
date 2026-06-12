"""Generated from Smithy shape ``com.amazonaws.connect#ContactMetricInfo``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_metric_name


class ContactMetricInfo(TypedDict):
    name: "aws_sdk_connect.types.contact_metric_name.ContactMetricName"
    """<p>The name of the metric to retrieve. Supported values are POSITION_IN_QUEUE (returns the contact's current position in the queue) and ESTIMATED_WAIT_TIME (returns the predicted wait time in seconds).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactMetricInfo) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.contact_metric_name

    out["Name"] = aws_sdk_connect.types.contact_metric_name.serialize_json(
        value["name"]
    )
    return out


def deserialize_json(data: dict) -> ContactMetricInfo:
    out: ContactMetricInfo = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_connect.types.contact_metric_name

        out["name"] = aws_sdk_connect.types.contact_metric_name.deserialize_json(
            data["Name"]
        )
    else:
        raise DeserializationError("ContactMetricInfo.name required")
    return out
