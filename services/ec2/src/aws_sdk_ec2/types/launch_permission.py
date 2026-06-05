"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchPermission``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.permission_group
    import aws_sdk_ec2.types.string


class LaunchPermission(TypedDict):
    organization_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of an organization.</p>"""
    organizational_unit_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of an organizational unit (OU).</p>"""
    user_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p> <p>Constraints: Up to 10 000 account IDs can be specified in a single request.</p>"""
    group: NotRequired["aws_sdk_ec2.types.permission_group.PermissionGroup"]
    """<p>The name of the group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchPermission, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "organization_arn" in value:
        pairs.append((f"{prefix}.OrganizationArn", str(value["organization_arn"])))
    if "organizational_unit_arn" in value:
        pairs.append(
            (f"{prefix}.OrganizationalUnitArn", str(value["organizational_unit_arn"]))
        )
    if "user_id" in value:
        pairs.append((f"{prefix}.UserId", str(value["user_id"])))
    if "group" in value:
        import aws_sdk_ec2.types.permission_group

        aws_sdk_ec2.types.permission_group.serialize_ec2_query(
            value["group"], pairs, f"{prefix}.Group"
        )


def deserialize_ec2_query(el: Element) -> LaunchPermission:
    out: LaunchPermission = {}  # type: ignore[typeddict-item]
    child_organization_arn = el.find("OrganizationArn")
    if child_organization_arn is not None:
        out["organization_arn"] = str(child_organization_arn.text or "")
    child_organizational_unit_arn = el.find("OrganizationalUnitArn")
    if child_organizational_unit_arn is not None:
        out["organizational_unit_arn"] = str(child_organizational_unit_arn.text or "")
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    child_group = el.find("Group")
    if child_group is not None:
        import aws_sdk_ec2.types.permission_group

        out["group"] = aws_sdk_ec2.types.permission_group.deserialize_ec2_query(
            child_group
        )
    return out
