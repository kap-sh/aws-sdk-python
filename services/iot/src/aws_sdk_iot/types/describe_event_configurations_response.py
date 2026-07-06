"""Generated from Smithy shape ``com.amazonaws.iot#DescribeEventConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.creation_date
    import aws_sdk_iot.types.event_configurations
    import aws_sdk_iot.types.last_modified_date


class DescribeEventConfigurationsResponse(TypedDict, closed=True):
    event_configurations: NotRequired[
        "aws_sdk_iot.types.event_configurations.EventConfigurations"
    ]
    """<p>The event configurations.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.creation_date.CreationDate"]
    """<p>The creation date of the event configuration.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_iot.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date the event configurations were last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEventConfigurationsResponse) -> dict:
    out: dict = {}
    if "event_configurations" in value:
        import aws_sdk_iot.types.event_configurations

        out["eventConfigurations"] = (
            aws_sdk_iot.types.event_configurations.serialize_json(
                value["event_configurations"]
            )
        )
    if "creation_date" in value:
        import aws_sdk_iot.types.creation_date

        out["creationDate"] = aws_sdk_iot.types.creation_date.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import aws_sdk_iot.types.last_modified_date

        out["lastModifiedDate"] = aws_sdk_iot.types.last_modified_date.serialize_json(
            value["last_modified_date"]
        )
    return out


def deserialize_json(data: dict) -> DescribeEventConfigurationsResponse:
    out: DescribeEventConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "eventConfigurations" in data:
        import aws_sdk_iot.types.event_configurations

        out["event_configurations"] = (
            aws_sdk_iot.types.event_configurations.deserialize_json(
                data["eventConfigurations"]
            )
        )
    if "creationDate" in data:
        import aws_sdk_iot.types.creation_date

        out["creation_date"] = aws_sdk_iot.types.creation_date.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import aws_sdk_iot.types.last_modified_date

        out["last_modified_date"] = (
            aws_sdk_iot.types.last_modified_date.deserialize_json(
                data["lastModifiedDate"]
            )
        )
    return out
