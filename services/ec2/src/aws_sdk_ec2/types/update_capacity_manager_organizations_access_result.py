"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateCapacityManagerOrganizationsAccessResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_manager_status


class UpdateCapacityManagerOrganizationsAccessResult(TypedDict):
    capacity_manager_status: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_status.CapacityManagerStatus"
    ]
    """<p> The current status of Capacity Manager after the update operation. </p>"""
    organizations_access: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> The updated Organizations access setting indicating whether cross-account data aggregation is enabled. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UpdateCapacityManagerOrganizationsAccessResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_manager_status" in value:
        import aws_sdk_ec2.types.capacity_manager_status

        aws_sdk_ec2.types.capacity_manager_status.serialize_ec2_query(
            value["capacity_manager_status"], pairs, f"{prefix}.CapacityManagerStatus"
        )
    if "organizations_access" in value:
        pairs.append(
            (
                f"{prefix}.OrganizationsAccess",
                "true" if value["organizations_access"] else "false",
            )
        )


def deserialize_ec2_query(
    el: Element,
) -> UpdateCapacityManagerOrganizationsAccessResult:
    out: UpdateCapacityManagerOrganizationsAccessResult = {}  # type: ignore[typeddict-item]
    child_capacity_manager_status = el.find("CapacityManagerStatus")
    if child_capacity_manager_status is not None:
        import aws_sdk_ec2.types.capacity_manager_status

        out["capacity_manager_status"] = (
            aws_sdk_ec2.types.capacity_manager_status.deserialize_ec2_query(
                child_capacity_manager_status
            )
        )
    child_organizations_access = el.find("OrganizationsAccess")
    if child_organizations_access is not None:
        out["organizations_access"] = (
            child_organizations_access.text or ""
        ).lower() == "true"
    return out
