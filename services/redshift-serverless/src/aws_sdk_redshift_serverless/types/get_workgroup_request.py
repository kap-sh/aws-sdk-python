"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetWorkgroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.workgroup_name


class GetWorkgroupRequest(TypedDict):
    workgroup_name: "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName"
    """<p>The name of the workgroup to return information for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkgroupRequest) -> dict:
    out: dict = {}
    out["workgroupName"] = value["workgroup_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkgroupRequest:
    out: GetWorkgroupRequest = {}  # type: ignore[typeddict-item]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    else:
        raise DeserializationError("GetWorkgroupRequest.workgroup_name required")
    return out
