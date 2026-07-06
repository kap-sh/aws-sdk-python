"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails(
    TypedDict, closed=True
):
    directory_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the Active Directory used for authentication. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails,
) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails:
    out: AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    return out
