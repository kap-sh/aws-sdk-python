"""Generated from Smithy shape ``com.amazonaws.signer#ListProfilePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signer.types.profile_name
    import aws_sdk_signer.types.string


class ListProfilePermissionsRequest(TypedDict):
    profile_name: "aws_sdk_signer.types.profile_name.ProfileName"
    """<p>Name of the signing profile containing the cross-account permissions.</p>"""
    next_token: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>String for specifying the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfilePermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProfilePermissionsRequest:
    out: ListProfilePermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
