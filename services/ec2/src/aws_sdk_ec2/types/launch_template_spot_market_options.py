"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateSpotMarketOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.instance_interruption_behavior
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.spot_instance_type
    import aws_sdk_ec2.types.string


class LaunchTemplateSpotMarketOptions(TypedDict, closed=True):
    max_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum hourly price you're willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price. If you do specify this parameter, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an <code>InvalidParameterValue</code> error message when the launch template is used to launch an instance.</p>"""
    spot_instance_type: NotRequired[
        "aws_sdk_ec2.types.spot_instance_type.SpotInstanceType"
    ]
    """<p>The Spot Instance request type.</p>"""
    block_duration_minutes: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The required duration for the Spot Instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360).</p>"""
    valid_until: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The end date of the request. For a one-time request, the request remains active until all instances launch, the request is canceled, or this date is reached. If the request is persistent, it remains active until it is canceled or this date and time is reached.</p>"""
    instance_interruption_behavior: NotRequired[
        "aws_sdk_ec2.types.instance_interruption_behavior.InstanceInterruptionBehavior"
    ]
    """<p>The behavior when a Spot Instance is interrupted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateSpotMarketOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "max_price" in value:
        pairs.append((f"{prefix}.MaxPrice", str(value["max_price"])))
    if "spot_instance_type" in value:
        import aws_sdk_ec2.types.spot_instance_type

        aws_sdk_ec2.types.spot_instance_type.serialize_ec2_query(
            value["spot_instance_type"], pairs, f"{prefix}.SpotInstanceType"
        )
    if "block_duration_minutes" in value:
        pairs.append(
            (f"{prefix}.BlockDurationMinutes", str(value["block_duration_minutes"]))
        )
    if "valid_until" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["valid_until"], pairs, f"{prefix}.ValidUntil"
        )
    if "instance_interruption_behavior" in value:
        import aws_sdk_ec2.types.instance_interruption_behavior

        aws_sdk_ec2.types.instance_interruption_behavior.serialize_ec2_query(
            value["instance_interruption_behavior"],
            pairs,
            f"{prefix}.InstanceInterruptionBehavior",
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateSpotMarketOptions:
    out: LaunchTemplateSpotMarketOptions = {}  # type: ignore[typeddict-item]
    child_max_price = el.find("MaxPrice")
    if child_max_price is not None:
        out["max_price"] = str(child_max_price.text or "")
    child_spot_instance_type = el.find("SpotInstanceType")
    if child_spot_instance_type is not None:
        import aws_sdk_ec2.types.spot_instance_type

        out["spot_instance_type"] = (
            aws_sdk_ec2.types.spot_instance_type.deserialize_ec2_query(
                child_spot_instance_type
            )
        )
    child_block_duration_minutes = el.find("BlockDurationMinutes")
    if child_block_duration_minutes is not None:
        out["block_duration_minutes"] = int(child_block_duration_minutes.text or "")
    child_valid_until = el.find("ValidUntil")
    if child_valid_until is not None:
        import aws_sdk_ec2.types.date_time

        out["valid_until"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_valid_until
        )
    child_instance_interruption_behavior = el.find("InstanceInterruptionBehavior")
    if child_instance_interruption_behavior is not None:
        import aws_sdk_ec2.types.instance_interruption_behavior

        out["instance_interruption_behavior"] = (
            aws_sdk_ec2.types.instance_interruption_behavior.deserialize_ec2_query(
                child_instance_interruption_behavior
            )
        )
    return out
