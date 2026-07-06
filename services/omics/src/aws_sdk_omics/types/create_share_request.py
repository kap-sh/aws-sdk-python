"""Generated from Smithy shape ``com.amazonaws.omics#CreateShareRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.share_name


class CreateShareRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource to be shared.</p>"""
    principal_subscriber: "str"
    """<p>The principal subscriber is the account being offered shared access to the resource. </p>"""
    share_name: NotRequired["aws_sdk_omics.types.share_name.ShareName"]
    """<p>A name that the owner defines for the share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateShareRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["principalSubscriber"] = value["principal_subscriber"]
    if "share_name" in value:
        out["shareName"] = value["share_name"]
    return out


def deserialize_json(data: dict) -> CreateShareRequest:
    out: CreateShareRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("CreateShareRequest.resource_arn required")
    if "principalSubscriber" in data:
        out["principal_subscriber"] = data["principalSubscriber"]
    else:
        raise DeserializationError("CreateShareRequest.principal_subscriber required")
    if "shareName" in data:
        out["share_name"] = data["shareName"]
    return out
