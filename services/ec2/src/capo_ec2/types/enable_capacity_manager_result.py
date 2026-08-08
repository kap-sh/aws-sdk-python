"""Generated from Smithy shape ``com.amazonaws.ec2#EnableCapacityManagerResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_manager_status


class EnableCapacityManagerResult(TypedDict, closed=True):
    capacity_manager_status: NotRequired[
        "capo_ec2.types.capacity_manager_status.CapacityManagerStatus"
    ]
    """<p> The current status of Capacity Manager after the enable operation. </p>"""
    organizations_access: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p> Indicates whether Organizations access is enabled for cross-account data aggregation. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableCapacityManagerResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_manager_status" in value:
        import capo_ec2.types.capacity_manager_status

        capo_ec2.types.capacity_manager_status.serialize_ec2_query(
            value["capacity_manager_status"],
            pairs,
            f"{key_prefix}CapacityManagerStatus",
        )
    if "organizations_access" in value:
        pairs.append(
            (
                f"{key_prefix}OrganizationsAccess",
                "true" if value["organizations_access"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> EnableCapacityManagerResult:
    out: EnableCapacityManagerResult = {}  # type: ignore[typeddict-item]
    child_capacity_manager_status = el.find("capacityManagerStatus")
    if child_capacity_manager_status is not None:
        import capo_ec2.types.capacity_manager_status

        out["capacity_manager_status"] = (
            capo_ec2.types.capacity_manager_status.deserialize_ec2_query(
                child_capacity_manager_status
            )
        )
    child_organizations_access = el.find("organizationsAccess")
    if child_organizations_access is not None:
        out["organizations_access"] = (
            child_organizations_access.text or ""
        ).lower() == "true"
    return out
