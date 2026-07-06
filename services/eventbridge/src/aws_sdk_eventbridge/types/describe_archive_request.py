"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeArchiveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.archive_name


class DescribeArchiveRequest(TypedDict, closed=True):
    archive_name: "aws_sdk_eventbridge.types.archive_name.ArchiveName"
    """<p>The name of the archive to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeArchiveRequest) -> dict:
    out: dict = {}
    out["ArchiveName"] = value["archive_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeArchiveRequest:
    out: DescribeArchiveRequest = {}  # type: ignore[typeddict-item]
    if "ArchiveName" in data:
        out["archive_name"] = data["ArchiveName"]
    else:
        raise DeserializationError("DescribeArchiveRequest.archive_name required")
    return out
