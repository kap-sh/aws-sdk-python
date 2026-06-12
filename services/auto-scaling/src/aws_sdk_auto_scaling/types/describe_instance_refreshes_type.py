"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeInstanceRefreshesType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.instance_refresh_ids
    import aws_sdk_auto_scaling.types.max_records
    import aws_sdk_auto_scaling.types.xml_string
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class DescribeInstanceRefreshesType(TypedDict):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    instance_refresh_ids: NotRequired[
        "aws_sdk_auto_scaling.types.instance_refresh_ids.InstanceRefreshIds"
    ]
    """<p>One or more instance refresh IDs.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_records: NotRequired["aws_sdk_auto_scaling.types.max_records.MaxRecords"]
    """<p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeInstanceRefreshesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "instance_refresh_ids" in value:
        import aws_sdk_auto_scaling.types.instance_refresh_ids

        aws_sdk_auto_scaling.types.instance_refresh_ids.serialize_query(
            value["instance_refresh_ids"], pairs, f"{prefix}.InstanceRefreshIds"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeInstanceRefreshesType:
    out: DescribeInstanceRefreshesType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_instance_refresh_ids = el.find("InstanceRefreshIds")
    if child_instance_refresh_ids is not None:
        import aws_sdk_auto_scaling.types.instance_refresh_ids

        out["instance_refresh_ids"] = (
            aws_sdk_auto_scaling.types.instance_refresh_ids.deserialize_query(
                child_instance_refresh_ids
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
