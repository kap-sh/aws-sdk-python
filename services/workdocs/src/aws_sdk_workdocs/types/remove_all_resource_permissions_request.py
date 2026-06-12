"""Generated from Smithy shape ``com.amazonaws.workdocs#RemoveAllResourcePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.resource_id_type


class RemoveAllResourcePermissionsRequest(TypedDict):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveAllResourcePermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveAllResourcePermissionsRequest:
    out: RemoveAllResourcePermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
