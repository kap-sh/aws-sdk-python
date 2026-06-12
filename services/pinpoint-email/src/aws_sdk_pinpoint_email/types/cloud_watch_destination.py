"""Generated from Smithy shape ``com.amazonaws.pinpointemail#CloudWatchDestination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.cloud_watch_dimension_configurations


class CloudWatchDestination(TypedDict):
    dimension_configurations: "aws_sdk_pinpoint_email.types.cloud_watch_dimension_configurations.CloudWatchDimensionConfigurations"
    """<p>An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchDestination) -> dict:
    out: dict = {}
    import aws_sdk_pinpoint_email.types.cloud_watch_dimension_configurations

    out["DimensionConfigurations"] = (
        aws_sdk_pinpoint_email.types.cloud_watch_dimension_configurations.serialize_json(
            value["dimension_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> CloudWatchDestination:
    out: CloudWatchDestination = {}  # type: ignore[typeddict-item]
    if "DimensionConfigurations" in data:
        import aws_sdk_pinpoint_email.types.cloud_watch_dimension_configurations

        out["dimension_configurations"] = (
            aws_sdk_pinpoint_email.types.cloud_watch_dimension_configurations.deserialize_json(
                data["DimensionConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "CloudWatchDestination.dimension_configurations required"
        )
    return out
