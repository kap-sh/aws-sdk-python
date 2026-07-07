"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeNotificationConfigurationsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.auto_scaling_group_names
    import aws_sdk_auto_scaling.types.max_records
    import aws_sdk_auto_scaling.types.xml_string


class DescribeNotificationConfigurationsType(TypedDict, closed=True):
    auto_scaling_group_names: NotRequired[
        "aws_sdk_auto_scaling.types.auto_scaling_group_names.AutoScalingGroupNames"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_records: NotRequired["aws_sdk_auto_scaling.types.max_records.MaxRecords"]
    """<p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeNotificationConfigurationsType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "auto_scaling_group_names" in value:
        import aws_sdk_auto_scaling.types.auto_scaling_group_names

        aws_sdk_auto_scaling.types.auto_scaling_group_names.serialize_query(
            value["auto_scaling_group_names"], pairs, f"{prefix}.AutoScalingGroupNames"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeNotificationConfigurationsType:
    out: DescribeNotificationConfigurationsType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_names = el.find("AutoScalingGroupNames")
    if child_auto_scaling_group_names is not None:
        import aws_sdk_auto_scaling.types.auto_scaling_group_names

        out["auto_scaling_group_names"] = (
            aws_sdk_auto_scaling.types.auto_scaling_group_names.deserialize_query(
                child_auto_scaling_group_names
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
