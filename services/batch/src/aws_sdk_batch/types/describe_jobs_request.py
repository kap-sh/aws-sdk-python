"""Generated from Smithy shape ``com.amazonaws.batch#DescribeJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string_list


class DescribeJobsRequest(TypedDict):
    jobs: NotRequired["aws_sdk_batch.types.string_list.StringList"]
    """<p>A list of up to 100 job IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobsRequest) -> dict:
    out: dict = {}
    if "jobs" in value:
        import aws_sdk_batch.types.string_list

        out["jobs"] = aws_sdk_batch.types.string_list.serialize_json(value["jobs"])
    return out


def deserialize_json(data: dict) -> DescribeJobsRequest:
    out: DescribeJobsRequest = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import aws_sdk_batch.types.string_list

        out["jobs"] = aws_sdk_batch.types.string_list.deserialize_json(data["jobs"])
    return out
