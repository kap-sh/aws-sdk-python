"""Generated from Smithy shape ``com.amazonaws.ec2#EnableInstanceSqlHaStandbyDetectionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.registered_instance_list


class EnableInstanceSqlHaStandbyDetectionsResult(TypedDict, closed=True):
    instances: NotRequired[
        "capo_ec2.types.registered_instance_list.RegisteredInstanceList"
    ]
    """<p>Information about the instances that were enabled for SQL Server High Availability standby detection monitoring.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableInstanceSqlHaStandbyDetectionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instances" in value:
        import capo_ec2.types.registered_instance_list

        capo_ec2.types.registered_instance_list.serialize_ec2_query(
            value["instances"], pairs, f"{key_prefix}InstanceSet"
        )


def deserialize_ec2_query(el: Element) -> EnableInstanceSqlHaStandbyDetectionsResult:
    out: EnableInstanceSqlHaStandbyDetectionsResult = {}  # type: ignore[typeddict-item]
    if el.find("InstanceSet") is not None:
        import capo_ec2.types.registered_instance_list

        out["instances"] = (
            capo_ec2.types.registered_instance_list.deserialize_ec2_query(
                el, "InstanceSet"
            )
        )
    return out
