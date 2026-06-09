"""Generated from Smithy shape ``com.amazonaws.ec2#SpotDatafeedSubscription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.datafeed_subscription_state
    import aws_sdk_ec2.types.spot_instance_state_fault
    import aws_sdk_ec2.types.string


class SpotDatafeedSubscription(TypedDict):
    bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket where the Spot Instance data feed is located.</p>"""
    fault: NotRequired[
        "aws_sdk_ec2.types.spot_instance_state_fault.SpotInstanceStateFault"
    ]
    """<p>The fault codes for the Spot Instance request, if any.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the account.</p>"""
    prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The prefix for the data feed files.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.datafeed_subscription_state.DatafeedSubscriptionState"
    ]
    """<p>The state of the Spot Instance data feed subscription.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotDatafeedSubscription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "bucket" in value:
        pairs.append((f"{prefix}.Bucket", str(value["bucket"])))
    if "fault" in value:
        import aws_sdk_ec2.types.spot_instance_state_fault

        aws_sdk_ec2.types.spot_instance_state_fault.serialize_ec2_query(
            value["fault"], pairs, f"{prefix}.Fault"
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "prefix" in value:
        pairs.append((f"{prefix}.Prefix", str(value["prefix"])))
    if "state" in value:
        import aws_sdk_ec2.types.datafeed_subscription_state

        aws_sdk_ec2.types.datafeed_subscription_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> SpotDatafeedSubscription:
    out: SpotDatafeedSubscription = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_fault = el.find("Fault")
    if child_fault is not None:
        import aws_sdk_ec2.types.spot_instance_state_fault

        out["fault"] = (
            aws_sdk_ec2.types.spot_instance_state_fault.deserialize_ec2_query(
                child_fault
            )
        )
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.datafeed_subscription_state

        out["state"] = (
            aws_sdk_ec2.types.datafeed_subscription_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
