"""Generated from Smithy shape ``com.amazonaws.ec2#RemoveIpamOrganizationalUnitExclusion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class RemoveIpamOrganizationalUnitExclusion(TypedDict):
    organizations_entity_path: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An Amazon Web Services Organizations entity path. Build the path for the OU(s) using Amazon Web Services Organizations IDs separated by a <code>/</code>. Include all child OUs by ending the path with <code>/*</code>.</p> <ul> <li> <p>Example 1</p> <ul> <li> <p>Path to a child OU: <code>o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/ou-jkl0-awsddddd/</code> </p> </li> <li> <p>In this example, <code>o-a1b2c3d4e5</code> is the organization ID, <code>r-f6g7h8i9j0example</code> is the root ID , <code>ou-ghi0-awsccccc</code> is an OU ID, and <code>ou-jkl0-awsddddd</code> is a child OU ID.</p> </li> <li> <p>IPAM will not manage the IP addresses in accounts in the child OU.</p> </li> </ul> </li> <li> <p>Example 2</p> <ul> <li> <p>Path where all child OUs will be part of the exclusion: <code>o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/*</code> </p> </li> <li> <p>In this example, IPAM will not manage the IP addresses in accounts in the OU (<code>ou-ghi0-awsccccc</code>) or in accounts in any OUs that are children of the OU.</p> </li> </ul> </li> </ul> <p>For more information on how to construct an entity path, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_access-advisor-viewing-orgs-entity-path\">Understand the Amazon Web Services Organizations entity path</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>"""
