"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpdatePackageGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeartifact.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.description
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.package_group_contact_info
    import aws_sdk_codeartifact.types.package_group_pattern


class UpdatePackageGroupRequest(TypedDict):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain which contains the package group to be updated. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    package_group: (
        "aws_sdk_codeartifact.types.package_group_pattern.PackageGroupPattern"
    )
    """<p> The pattern of the package group to be updated. </p>"""
    contact_info: NotRequired[
        "aws_sdk_codeartifact.types.package_group_contact_info.PackageGroupContactInfo"
    ]
    """<p> Contact information which you want to update the requested package group with. </p>"""
    description: NotRequired["aws_sdk_codeartifact.types.description.Description"]
    """<p> The description you want to update the requested package group with. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageGroupRequest) -> dict:
    out: dict = {}
    out["packageGroup"] = value["package_group"]
    if "contact_info" in value:
        out["contactInfo"] = value["contact_info"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdatePackageGroupRequest:
    out: UpdatePackageGroupRequest = {}  # type: ignore[typeddict-item]
    if "packageGroup" in data:
        out["package_group"] = data["packageGroup"]
    else:
        raise DeserializationError("UpdatePackageGroupRequest.package_group required")
    if "contactInfo" in data:
        out["contact_info"] = data["contactInfo"]
    if "description" in data:
        out["description"] = data["description"]
    return out
