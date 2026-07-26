"""Generated from Smithy shape ``com.amazonaws.fsx#DetachAndDeleteS3AccessPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.client_request_token
    import capo_fsx.types.s3_access_point_attachment_name


class DetachAndDeleteS3AccessPointRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    name: NotRequired[
        "capo_fsx.types.s3_access_point_attachment_name.S3AccessPointAttachmentName"
    ]
    """<p>The name of the S3 access point attachment that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetachAndDeleteS3AccessPointRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetachAndDeleteS3AccessPointRequest:
    out: DetachAndDeleteS3AccessPointRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
