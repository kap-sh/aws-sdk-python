"""Generated from Smithy shape ``com.amazonaws.location#DeleteKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.resource_name


class DeleteKeyRequest(TypedDict, closed=True):
    key_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the API key to delete.</p>"""
    force_delete: NotRequired["bool"]
    """<p>ForceDelete bypasses an API key's expiry conditions and deletes the key. Set the parameter <code>true</code> to delete the key or to <code>false</code> to not preemptively delete the API key.</p> <p>Valid values: <code>true</code>, or <code>false</code>.</p> <p>Required: No</p> <note> <p>This action is irreversible. Only use ForceDelete if you are certain the key is no longer in use.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKeyRequest:
    out: DeleteKeyRequest = {}  # type: ignore[typeddict-item]
    return out
