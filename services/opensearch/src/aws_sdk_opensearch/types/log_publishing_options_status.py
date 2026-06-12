"""Generated from Smithy shape ``com.amazonaws.opensearch#LogPublishingOptionsStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.log_publishing_options
    import aws_sdk_opensearch.types.option_status


class LogPublishingOptionsStatus(TypedDict):
    options: NotRequired[
        "aws_sdk_opensearch.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>The log publishing options configured for the domain.</p>"""
    status: NotRequired["aws_sdk_opensearch.types.option_status.OptionStatus"]
    """<p>The status of the log publishing options for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogPublishingOptionsStatus) -> dict:
    out: dict = {}
    if "options" in value:
        import aws_sdk_opensearch.types.log_publishing_options

        out["Options"] = aws_sdk_opensearch.types.log_publishing_options.serialize_json(
            value["options"]
        )
    if "status" in value:
        import aws_sdk_opensearch.types.option_status

        out["Status"] = aws_sdk_opensearch.types.option_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> LogPublishingOptionsStatus:
    out: LogPublishingOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_opensearch.types.log_publishing_options

        out["options"] = (
            aws_sdk_opensearch.types.log_publishing_options.deserialize_json(
                data["Options"]
            )
        )
    if "Status" in data:
        import aws_sdk_opensearch.types.option_status

        out["status"] = aws_sdk_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    return out
