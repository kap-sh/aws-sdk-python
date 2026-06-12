"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.arn
    import aws_sdk_codeartifact.types.description
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.package_group_contact_info
    import aws_sdk_codeartifact.types.package_group_origin_configuration
    import aws_sdk_codeartifact.types.package_group_pattern
    import aws_sdk_codeartifact.types.package_group_reference
    import aws_sdk_codeartifact.types.timestamp


class PackageGroupSummary(TypedDict):
    arn: NotRequired["aws_sdk_codeartifact.types.arn.Arn"]
    """<p> The ARN of the package group. </p>"""
    pattern: NotRequired[
        "aws_sdk_codeartifact.types.package_group_pattern.PackageGroupPattern"
    ]
    """<p> The pattern of the package group. The pattern determines which packages are associated with the package group. </p>"""
    domain_name: NotRequired["aws_sdk_codeartifact.types.domain_name.DomainName"]
    """<p> The domain that contains the package group. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    created_time: NotRequired["aws_sdk_codeartifact.types.timestamp.Timestamp"]
    """<p>A timestamp that represents the date and time the repository was created.</p>"""
    contact_info: NotRequired[
        "aws_sdk_codeartifact.types.package_group_contact_info.PackageGroupContactInfo"
    ]
    """<p> The contact information of the package group. </p>"""
    description: NotRequired["aws_sdk_codeartifact.types.description.Description"]
    """<p> The description of the package group. </p>"""
    origin_configuration: NotRequired[
        "aws_sdk_codeartifact.types.package_group_origin_configuration.PackageGroupOriginConfiguration"
    ]
    """<p>Details about the package origin configuration of a package group.</p>"""
    parent: NotRequired[
        "aws_sdk_codeartifact.types.package_group_reference.PackageGroupReference"
    ]
    """<p> The direct parent package group of the package group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "pattern" in value:
        out["pattern"] = value["pattern"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "domain_owner" in value:
        out["domainOwner"] = value["domain_owner"]
    if "created_time" in value:
        import aws_sdk_codeartifact.types.timestamp

        out["createdTime"] = aws_sdk_codeartifact.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "contact_info" in value:
        out["contactInfo"] = value["contact_info"]
    if "description" in value:
        out["description"] = value["description"]
    if "origin_configuration" in value:
        import aws_sdk_codeartifact.types.package_group_origin_configuration

        out["originConfiguration"] = (
            aws_sdk_codeartifact.types.package_group_origin_configuration.serialize_json(
                value["origin_configuration"]
            )
        )
    if "parent" in value:
        import aws_sdk_codeartifact.types.package_group_reference

        out["parent"] = (
            aws_sdk_codeartifact.types.package_group_reference.serialize_json(
                value["parent"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageGroupSummary:
    out: PackageGroupSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "pattern" in data:
        out["pattern"] = data["pattern"]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "domainOwner" in data:
        out["domain_owner"] = data["domainOwner"]
    if "createdTime" in data:
        import aws_sdk_codeartifact.types.timestamp

        out["created_time"] = aws_sdk_codeartifact.types.timestamp.deserialize_json(
            data["createdTime"]
        )
    if "contactInfo" in data:
        out["contact_info"] = data["contactInfo"]
    if "description" in data:
        out["description"] = data["description"]
    if "originConfiguration" in data:
        import aws_sdk_codeartifact.types.package_group_origin_configuration

        out["origin_configuration"] = (
            aws_sdk_codeartifact.types.package_group_origin_configuration.deserialize_json(
                data["originConfiguration"]
            )
        )
    if "parent" in data:
        import aws_sdk_codeartifact.types.package_group_reference

        out["parent"] = (
            aws_sdk_codeartifact.types.package_group_reference.deserialize_json(
                data["parent"]
            )
        )
    return out
