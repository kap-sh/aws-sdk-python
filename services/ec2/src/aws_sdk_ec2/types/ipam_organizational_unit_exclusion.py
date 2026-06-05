"""Generated from Smithy shape ``com.amazonaws.ec2#IpamOrganizationalUnitExclusion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class IpamOrganizationalUnitExclusion(TypedDict):
    organizations_entity_path: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An Amazon Web Services Organizations entity path. For more information on the entity path, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_access-advisor-viewing-orgs-entity-path\">Understand the Amazon Web Services Organizations entity path</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamOrganizationalUnitExclusion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "organizations_entity_path" in value:
        pairs.append(
            (
                f"{prefix}.OrganizationsEntityPath",
                str(value["organizations_entity_path"]),
            )
        )


def deserialize_ec2_query(el: Element) -> IpamOrganizationalUnitExclusion:
    out: IpamOrganizationalUnitExclusion = {}  # type: ignore[typeddict-item]
    child_organizations_entity_path = el.find("OrganizationsEntityPath")
    if child_organizations_entity_path is not None:
        out["organizations_entity_path"] = str(
            child_organizations_entity_path.text or ""
        )
    return out
