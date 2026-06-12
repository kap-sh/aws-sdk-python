"""Generated from Smithy shape ``com.amazonaws.emr#EMRContainersConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.xml_string_max_len256


class EMRContainersConfig(TypedDict):
    job_run_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The Job run ID for the container configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EMRContainersConfig) -> dict:
    out: dict = {}
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EMRContainersConfig:
    out: EMRContainersConfig = {}  # type: ignore[typeddict-item]
    if "JobRunId" in data:
        out["job_run_id"] = data["JobRunId"]
    return out
