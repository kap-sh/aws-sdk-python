"""Generated from Smithy shape ``com.amazonaws.autoscaling#AutoScalingGroupNamesType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.auto_scaling_group_names
    import aws_sdk_auto_scaling.types.filters
    import aws_sdk_auto_scaling.types.include_instances
    import aws_sdk_auto_scaling.types.max_records
    import aws_sdk_auto_scaling.types.xml_string


class AutoScalingGroupNamesType(TypedDict):
    auto_scaling_group_names: NotRequired[
        "aws_sdk_auto_scaling.types.auto_scaling_group_names.AutoScalingGroupNames"
    ]
    """<p>The names of the Auto Scaling groups. By default, you can only specify up to 50 names. You can optionally increase this limit using the <code>MaxRecords</code> property.</p> <p>If you omit this property, all Auto Scaling groups are described.</p>"""
    include_instances: NotRequired[
        "aws_sdk_auto_scaling.types.include_instances.IncludeInstances"
    ]
    """<p> Specifies whether to include information about Amazon EC2 instances in the response. When set to <code>true</code> (default), the response includes instance details. </p>"""
    next_token: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_records: NotRequired["aws_sdk_auto_scaling.types.max_records.MaxRecords"]
    """<p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p>"""
    filters: NotRequired["aws_sdk_auto_scaling.types.filters.Filters"]
    """<p>One or more filters to limit the results based on specific tags. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AutoScalingGroupNamesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_names" in value:
        import aws_sdk_auto_scaling.types.auto_scaling_group_names

        aws_sdk_auto_scaling.types.auto_scaling_group_names.serialize_query(
            value["auto_scaling_group_names"], pairs, f"{prefix}.AutoScalingGroupNames"
        )
    if "include_instances" in value:
        pairs.append(
            (
                f"{prefix}.IncludeInstances",
                "true" if value["include_instances"] else "false",
            )
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "filters" in value:
        import aws_sdk_auto_scaling.types.filters

        aws_sdk_auto_scaling.types.filters.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )


def deserialize_query(el: Element) -> AutoScalingGroupNamesType:
    out: AutoScalingGroupNamesType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_names = el.find("AutoScalingGroupNames")
    if child_auto_scaling_group_names is not None:
        import aws_sdk_auto_scaling.types.auto_scaling_group_names

        out["auto_scaling_group_names"] = (
            aws_sdk_auto_scaling.types.auto_scaling_group_names.deserialize_query(
                child_auto_scaling_group_names
            )
        )
    child_include_instances = el.find("IncludeInstances")
    if child_include_instances is not None:
        out["include_instances"] = (
            child_include_instances.text or ""
        ).lower() == "true"
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_auto_scaling.types.filters

        out["filters"] = aws_sdk_auto_scaling.types.filters.deserialize_query(
            child_filters
        )
    return out
