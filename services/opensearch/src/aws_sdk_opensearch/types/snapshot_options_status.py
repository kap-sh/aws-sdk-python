"""Generated from Smithy shape ``com.amazonaws.opensearch#SnapshotOptionsStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.option_status
    import aws_sdk_opensearch.types.snapshot_options


class SnapshotOptionsStatus(TypedDict):
    options: "aws_sdk_opensearch.types.snapshot_options.SnapshotOptions"
    """<p>The daily snapshot options specified for the domain.</p>"""
    status: "aws_sdk_opensearch.types.option_status.OptionStatus"
    """<p>The status of a daily automated snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotOptionsStatus) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.snapshot_options

    out["Options"] = aws_sdk_opensearch.types.snapshot_options.serialize_json(
        value["options"]
    )
    import aws_sdk_opensearch.types.option_status

    out["Status"] = aws_sdk_opensearch.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> SnapshotOptionsStatus:
    out: SnapshotOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_opensearch.types.snapshot_options

        out["options"] = aws_sdk_opensearch.types.snapshot_options.deserialize_json(
            data["Options"]
        )
    else:
        raise DeserializationError("SnapshotOptionsStatus.options required")
    if "Status" in data:
        import aws_sdk_opensearch.types.option_status

        out["status"] = aws_sdk_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("SnapshotOptionsStatus.status required")
    return out
