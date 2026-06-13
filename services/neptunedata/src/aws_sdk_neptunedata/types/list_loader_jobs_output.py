"""Generated from Smithy shape ``com.amazonaws.neptunedata#ListLoaderJobsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_neptunedata.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.loader_id_result


class ListLoaderJobsOutput(TypedDict):
    status: "str"
    """<p>Returns the status of the job list request.</p>"""
    payload: "aws_sdk_neptunedata.types.loader_id_result.LoaderIdResult"
    """<p>The requested list of job IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLoaderJobsOutput) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    import aws_sdk_neptunedata.types.loader_id_result

    out["payload"] = aws_sdk_neptunedata.types.loader_id_result.serialize_json(
        value["payload"]
    )
    return out


def deserialize_json(data: dict) -> ListLoaderJobsOutput:
    out: ListLoaderJobsOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ListLoaderJobsOutput.status required")
    if "payload" in data:
        import aws_sdk_neptunedata.types.loader_id_result

        out["payload"] = aws_sdk_neptunedata.types.loader_id_result.deserialize_json(
            data["payload"]
        )
    else:
        raise DeserializationError("ListLoaderJobsOutput.payload required")
    return out
