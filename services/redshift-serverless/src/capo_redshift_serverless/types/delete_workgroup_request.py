"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteWorkgroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.workgroup_name


class DeleteWorkgroupRequest(TypedDict, closed=True):
    workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName"
    """<p>The name of the workgroup to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkgroupRequest) -> dict:
    out: dict = {}
    out["workgroupName"] = value["workgroup_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkgroupRequest:
    out: DeleteWorkgroupRequest = {}  # type: ignore[typeddict-item]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    else:
        raise DeserializationError("DeleteWorkgroupRequest.workgroup_name required")
    return out
