"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFleetResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_fleet_errors_set
    import aws_sdk_ec2.types.create_fleet_instances_set
    import aws_sdk_ec2.types.fleet_id


class CreateFleetResult(TypedDict):
    fleet_id: NotRequired["aws_sdk_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC2 Fleet.</p>"""
    errors: NotRequired[
        "aws_sdk_ec2.types.create_fleet_errors_set.CreateFleetErrorsSet"
    ]
    """<p>Information about the instances that could not be launched by the fleet. Supported only for fleets of type <code>instant</code>.</p>"""
    instances: NotRequired[
        "aws_sdk_ec2.types.create_fleet_instances_set.CreateFleetInstancesSet"
    ]
    """<p>Information about the instances that were launched by the fleet. Supported only for fleets of type <code>instant</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateFleetResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "fleet_id" in value:
        pairs.append((f"{prefix}.FleetId", str(value["fleet_id"])))
    if "errors" in value:
        import aws_sdk_ec2.types.create_fleet_errors_set

        aws_sdk_ec2.types.create_fleet_errors_set.serialize_ec2_query(
            value["errors"], pairs, f"{prefix}.ErrorSet"
        )
    if "instances" in value:
        import aws_sdk_ec2.types.create_fleet_instances_set

        aws_sdk_ec2.types.create_fleet_instances_set.serialize_ec2_query(
            value["instances"], pairs, f"{prefix}.FleetInstanceSet"
        )


def deserialize_ec2_query(el: Element) -> CreateFleetResult:
    out: CreateFleetResult = {}  # type: ignore[typeddict-item]
    child_fleet_id = el.find("FleetId")
    if child_fleet_id is not None:
        out["fleet_id"] = str(child_fleet_id.text or "")
    if el.find("ErrorSet") is not None:
        import aws_sdk_ec2.types.create_fleet_errors_set

        out["errors"] = aws_sdk_ec2.types.create_fleet_errors_set.deserialize_ec2_query(
            el, "ErrorSet"
        )
    if el.find("FleetInstanceSet") is not None:
        import aws_sdk_ec2.types.create_fleet_instances_set

        out["instances"] = (
            aws_sdk_ec2.types.create_fleet_instances_set.deserialize_ec2_query(
                el, "FleetInstanceSet"
            )
        )
    return out
