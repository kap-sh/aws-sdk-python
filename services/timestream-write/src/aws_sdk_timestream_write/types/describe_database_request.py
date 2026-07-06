"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DescribeDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.resource_name


class DescribeDatabaseRequest(TypedDict, closed=True):
    database_name: "aws_sdk_timestream_write.types.resource_name.ResourceName"
    """<p>The name of the Timestream database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeDatabaseRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeDatabaseRequest:
    out: DescribeDatabaseRequest = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("DescribeDatabaseRequest.database_name required")
    return out
