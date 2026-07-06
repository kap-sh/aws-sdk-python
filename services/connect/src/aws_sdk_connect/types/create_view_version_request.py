"""Generated from Smithy shape ``com.amazonaws.connect#CreateViewVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.view_content_sha256
    import aws_sdk_connect.types.view_description
    import aws_sdk_connect.types.view_id
    import aws_sdk_connect.types.views_instance_id


class CreateViewVersionRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.views_instance_id.ViewsInstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.</p>"""
    view_id: "aws_sdk_connect.types.view_id.ViewId"
    """<p>The identifier of the view. Both <code>ViewArn</code> and <code>ViewId</code> can be used.</p>"""
    version_description: NotRequired[
        "aws_sdk_connect.types.view_description.ViewDescription"
    ]
    """<p>The description for the version being published.</p>"""
    view_content_sha256: NotRequired[
        "aws_sdk_connect.types.view_content_sha256.ViewContentSha256"
    ]
    """<p>Indicates the checksum value of the latest published view content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateViewVersionRequest) -> dict:
    out: dict = {}
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "view_content_sha256" in value:
        out["ViewContentSha256"] = value["view_content_sha256"]
    return out


def deserialize_json(data: dict) -> CreateViewVersionRequest:
    out: CreateViewVersionRequest = {}  # type: ignore[typeddict-item]
    if "VersionDescription" in data:
        out["version_description"] = data["VersionDescription"]
    if "ViewContentSha256" in data:
        out["view_content_sha256"] = data["ViewContentSha256"]
    return out
