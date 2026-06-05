"""Generated from Smithy shape ``com.amazonaws.ec2#EnableInstanceSqlHaStandbyDetectionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.registered_instance_list


class EnableInstanceSqlHaStandbyDetectionsResult(TypedDict):
    instances: NotRequired[
        "aws_sdk_ec2.types.registered_instance_list.RegisteredInstanceList"
    ]
    """<p>Information about the instances that were enabled for SQL Server High Availability standby detection monitoring.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableInstanceSqlHaStandbyDetectionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instances" in value:
        import aws_sdk_ec2.types.registered_instance_list

        aws_sdk_ec2.types.registered_instance_list.serialize_ec2_query(
            value["instances"], pairs, f"{prefix}.InstanceSet"
        )


def deserialize_ec2_query(el: Element) -> EnableInstanceSqlHaStandbyDetectionsResult:
    out: EnableInstanceSqlHaStandbyDetectionsResult = {}  # type: ignore[typeddict-item]
    if el.find("InstanceSet") is not None:
        import aws_sdk_ec2.types.registered_instance_list

        out["instances"] = (
            aws_sdk_ec2.types.registered_instance_list.deserialize_ec2_query(
                el, "InstanceSet"
            )
        )
    return out
