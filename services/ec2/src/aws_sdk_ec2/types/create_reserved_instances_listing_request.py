"""Generated from Smithy shape ``com.amazonaws.ec2#CreateReservedInstancesListingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.price_schedule_specification_list
    import aws_sdk_ec2.types.reservation_id
    import aws_sdk_ec2.types.string


class CreateReservedInstancesListingRequest(TypedDict):
    reserved_instances_id: NotRequired["aws_sdk_ec2.types.reservation_id.ReservationId"]
    """<p>The ID of the active Standard Reserved Instance.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances that are a part of a Reserved Instance account to be listed in the Reserved Instance Marketplace. This number should be less than or equal to the instance count associated with the Reserved Instance ID specified in this call.</p>"""
    price_schedules: NotRequired[
        "aws_sdk_ec2.types.price_schedule_specification_list.PriceScheduleSpecificationList"
    ]
    """<p>A list specifying the price of the Standard Reserved Instance for each month remaining in the Reserved Instance term.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier you provide to ensure idempotency of your listings. This helps avoid duplicate listings. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateReservedInstancesListingRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "reserved_instances_id" in value:
        pairs.append(
            (f"{prefix}.ReservedInstancesId", str(value["reserved_instances_id"]))
        )
    if "instance_count" in value:
        pairs.append((f"{prefix}.InstanceCount", str(value["instance_count"])))
    if "price_schedules" in value:
        import aws_sdk_ec2.types.price_schedule_specification_list

        aws_sdk_ec2.types.price_schedule_specification_list.serialize_ec2_query(
            value["price_schedules"], pairs, f"{prefix}.PriceSchedules"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateReservedInstancesListingRequest:
    out: CreateReservedInstancesListingRequest = {}  # type: ignore[typeddict-item]
    child_reserved_instances_id = el.find("ReservedInstancesId")
    if child_reserved_instances_id is not None:
        out["reserved_instances_id"] = str(child_reserved_instances_id.text or "")
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    if el.find("PriceSchedules") is not None:
        import aws_sdk_ec2.types.price_schedule_specification_list

        out["price_schedules"] = (
            aws_sdk_ec2.types.price_schedule_specification_list.deserialize_ec2_query(
                el, "PriceSchedules"
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
