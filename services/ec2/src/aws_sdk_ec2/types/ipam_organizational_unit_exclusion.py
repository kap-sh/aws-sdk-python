"""Generated from Smithy shape ``com.amazonaws.ec2#IpamOrganizationalUnitExclusion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class IpamOrganizationalUnitExclusion(TypedDict):
    organizations_entity_path: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An Amazon Web Services Organizations entity path. For more information on the entity path, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_access-advisor-viewing-orgs-entity-path\">Understand the Amazon Web Services Organizations entity path</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>"""
