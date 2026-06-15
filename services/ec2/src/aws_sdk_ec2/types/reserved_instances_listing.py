"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesListing``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.instance_count_list
    import aws_sdk_ec2.types.listing_status
    import aws_sdk_ec2.types.price_schedule_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ReservedInstancesListing(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    r"""<p>A unique, case-sensitive key supplied by the client to ensure that the request is idempotent. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
    create_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time the listing was created.</p>"""
    instance_counts: NotRequired[
        "aws_sdk_ec2.types.instance_count_list.InstanceCountList"
    ]
    """<p>The number of instances in this state.</p>"""
    price_schedules: NotRequired[
        "aws_sdk_ec2.types.price_schedule_list.PriceScheduleList"
    ]
    """<p>The price of the Reserved Instance listing.</p>"""
    reserved_instances_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance.</p>"""
    reserved_instances_listing_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance listing.</p>"""
    status: NotRequired["aws_sdk_ec2.types.listing_status.ListingStatus"]
    """<p>The status of the Reserved Instance listing.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the current status of the Reserved Instance listing. The response can be blank.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the resource.</p>"""
    update_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The last modified timestamp of the listing.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesListing, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "create_date" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )
    if "instance_counts" in value:
        import aws_sdk_ec2.types.instance_count_list

        aws_sdk_ec2.types.instance_count_list.serialize_ec2_query(
            value["instance_counts"], pairs, f"{prefix}.InstanceCounts"
        )
    if "price_schedules" in value:
        import aws_sdk_ec2.types.price_schedule_list

        aws_sdk_ec2.types.price_schedule_list.serialize_ec2_query(
            value["price_schedules"], pairs, f"{prefix}.PriceSchedules"
        )
    if "reserved_instances_id" in value:
        pairs.append(
            (f"{prefix}.ReservedInstancesId", str(value["reserved_instances_id"]))
        )
    if "reserved_instances_listing_id" in value:
        pairs.append(
            (
                f"{prefix}.ReservedInstancesListingId",
                str(value["reserved_instances_listing_id"]),
            )
        )
    if "status" in value:
        import aws_sdk_ec2.types.listing_status

        aws_sdk_ec2.types.listing_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "update_date" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["update_date"], pairs, f"{prefix}.UpdateDate"
        )


def deserialize_ec2_query(el: Element) -> ReservedInstancesListing:
    out: ReservedInstancesListing = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_ec2.types.date_time

        out["create_date"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_create_date
        )
    if el.find("InstanceCounts") is not None:
        import aws_sdk_ec2.types.instance_count_list

        out["instance_counts"] = (
            aws_sdk_ec2.types.instance_count_list.deserialize_ec2_query(
                el, "InstanceCounts"
            )
        )
    if el.find("PriceSchedules") is not None:
        import aws_sdk_ec2.types.price_schedule_list

        out["price_schedules"] = (
            aws_sdk_ec2.types.price_schedule_list.deserialize_ec2_query(
                el, "PriceSchedules"
            )
        )
    child_reserved_instances_id = el.find("ReservedInstancesId")
    if child_reserved_instances_id is not None:
        out["reserved_instances_id"] = str(child_reserved_instances_id.text or "")
    child_reserved_instances_listing_id = el.find("ReservedInstancesListingId")
    if child_reserved_instances_listing_id is not None:
        out["reserved_instances_listing_id"] = str(
            child_reserved_instances_listing_id.text or ""
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.listing_status

        out["status"] = aws_sdk_ec2.types.listing_status.deserialize_ec2_query(
            child_status
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_update_date = el.find("UpdateDate")
    if child_update_date is not None:
        import aws_sdk_ec2.types.date_time

        out["update_date"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_update_date
        )
    return out
