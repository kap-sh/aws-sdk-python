"""Generated from Smithy shape ``com.amazonaws.inspector2#Ec2InstanceAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.ec2_instance_sort_by
    import aws_sdk_inspector2.types.map_filter_list
    import aws_sdk_inspector2.types.sort_order
    import aws_sdk_inspector2.types.string_filter_list


class Ec2InstanceAggregation(TypedDict):
    amis: NotRequired["aws_sdk_inspector2.types.string_filter_list.StringFilterList"]
    """<p>The AMI IDs associated with the Amazon EC2 instances to aggregate findings for.</p>"""
    operating_systems: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The operating system types to aggregate findings for. Valid values must be uppercase and underscore separated, examples are <code>ORACLE_LINUX_7</code> and <code>ALPINE_LINUX_3_8</code>.</p>"""
    instance_ids: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The Amazon EC2 instance IDs to aggregate findings for.</p>"""
    instance_tags: NotRequired["aws_sdk_inspector2.types.map_filter_list.MapFilterList"]
    """<p>The Amazon EC2 instance tags to aggregate findings for.</p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.sort_order.SortOrder"]
    """<p>The order to sort results by.</p>"""
    sort_by: NotRequired[
        "aws_sdk_inspector2.types.ec2_instance_sort_by.Ec2InstanceSortBy"
    ]
    """<p>The value to sort results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2InstanceAggregation) -> dict:
    out: dict = {}
    if "amis" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["amis"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["amis"]
        )
    if "operating_systems" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["operatingSystems"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["operating_systems"]
            )
        )
    if "instance_ids" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["instanceIds"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["instance_ids"]
        )
    if "instance_tags" in value:
        import aws_sdk_inspector2.types.map_filter_list

        out["instanceTags"] = aws_sdk_inspector2.types.map_filter_list.serialize_json(
            value["instance_tags"]
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    return out


def deserialize_json(data: dict) -> Ec2InstanceAggregation:
    out: Ec2InstanceAggregation = {}  # type: ignore[typeddict-item]
    if "amis" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["amis"] = aws_sdk_inspector2.types.string_filter_list.deserialize_json(
            data["amis"]
        )
    if "operatingSystems" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["operating_systems"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["operatingSystems"]
            )
        )
    if "instanceIds" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["instance_ids"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["instanceIds"]
            )
        )
    if "instanceTags" in data:
        import aws_sdk_inspector2.types.map_filter_list

        out["instance_tags"] = (
            aws_sdk_inspector2.types.map_filter_list.deserialize_json(
                data["instanceTags"]
            )
        )
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    return out
