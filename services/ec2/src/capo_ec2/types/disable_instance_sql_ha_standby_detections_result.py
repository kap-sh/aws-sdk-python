"""Generated from Smithy shape ``com.amazonaws.ec2#DisableInstanceSqlHaStandbyDetectionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.registered_instance_list


class DisableInstanceSqlHaStandbyDetectionsResult(TypedDict, closed=True):
    instances: NotRequired[
        "capo_ec2.types.registered_instance_list.RegisteredInstanceList"
    ]
    """<p>Information about the instances that were disabled from SQL Server High Availability standby detection monitoring.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableInstanceSqlHaStandbyDetectionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instances" in value:
        import capo_ec2.types.registered_instance_list

        capo_ec2.types.registered_instance_list.serialize_ec2_query(
            value["instances"], pairs, f"{key_prefix}InstanceSet"
        )


def deserialize_ec2_query(el: Element) -> DisableInstanceSqlHaStandbyDetectionsResult:
    out: DisableInstanceSqlHaStandbyDetectionsResult = {}  # type: ignore[typeddict-item]
    child_instances = el.find("instanceSet")
    if child_instances is not None:
        import capo_ec2.types.registered_instance_list

        out["instances"] = (
            capo_ec2.types.registered_instance_list.deserialize_ec2_query(
                child_instances
            )
        )
    return out
