"""Generated from Smithy shape ``com.amazonaws.panorama#CreateJobForDevicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.job_list


class CreateJobForDevicesResponse(TypedDict, closed=True):
    jobs: "aws_sdk_panorama.types.job_list.JobList"
    """<p>A list of jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobForDevicesResponse) -> dict:
    out: dict = {}
    import aws_sdk_panorama.types.job_list

    out["Jobs"] = aws_sdk_panorama.types.job_list.serialize_json(value["jobs"])
    return out


def deserialize_json(data: dict) -> CreateJobForDevicesResponse:
    out: CreateJobForDevicesResponse = {}  # type: ignore[typeddict-item]
    if "Jobs" in data:
        import aws_sdk_panorama.types.job_list

        out["jobs"] = aws_sdk_panorama.types.job_list.deserialize_json(data["Jobs"])
    else:
        raise DeserializationError("CreateJobForDevicesResponse.jobs required")
    return out
