"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLaunchTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_launch_templates_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.launch_template_id_string_list
    import aws_sdk_ec2.types.launch_template_name_string_list
    import aws_sdk_ec2.types.string


class DescribeLaunchTemplatesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    launch_template_ids: NotRequired[
        "aws_sdk_ec2.types.launch_template_id_string_list.LaunchTemplateIdStringList"
    ]
    """<p>One or more launch template IDs.</p>"""
    launch_template_names: NotRequired[
        "aws_sdk_ec2.types.launch_template_name_string_list.LaunchTemplateNameStringList"
    ]
    """<p>One or more launch template names.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>create-time</code> - The time the launch template was created.</p> </li> <li> <p> <code>launch-template-name</code> - The name of the launch template.</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to request the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_launch_templates_max_results.DescribeLaunchTemplatesMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. This value can be between 1 and 200.</p>"""
    include_managed_resources: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to include managed resources in the output. If this parameter is set to <code>true</code>, the output includes resources that are managed by Amazon Web Services services, even if managed resource visibility is set to hidden.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLaunchTemplatesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "launch_template_ids" in value:
        import aws_sdk_ec2.types.launch_template_id_string_list

        aws_sdk_ec2.types.launch_template_id_string_list.serialize_ec2_query(
            value["launch_template_ids"], pairs, f"{prefix}.LaunchTemplateIds"
        )
    if "launch_template_names" in value:
        import aws_sdk_ec2.types.launch_template_name_string_list

        aws_sdk_ec2.types.launch_template_name_string_list.serialize_ec2_query(
            value["launch_template_names"], pairs, f"{prefix}.LaunchTemplateNames"
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "include_managed_resources" in value:
        pairs.append(
            (
                f"{prefix}.IncludeManagedResources",
                "true" if value["include_managed_resources"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> DescribeLaunchTemplatesRequest:
    out: DescribeLaunchTemplatesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("LaunchTemplateIds") is not None:
        import aws_sdk_ec2.types.launch_template_id_string_list

        out["launch_template_ids"] = (
            aws_sdk_ec2.types.launch_template_id_string_list.deserialize_ec2_query(
                el, "LaunchTemplateIds"
            )
        )
    if el.find("LaunchTemplateNames") is not None:
        import aws_sdk_ec2.types.launch_template_name_string_list

        out["launch_template_names"] = (
            aws_sdk_ec2.types.launch_template_name_string_list.deserialize_ec2_query(
                el, "LaunchTemplateNames"
            )
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_include_managed_resources = el.find("IncludeManagedResources")
    if child_include_managed_resources is not None:
        out["include_managed_resources"] = (
            child_include_managed_resources.text or ""
        ).lower() == "true"
    return out
