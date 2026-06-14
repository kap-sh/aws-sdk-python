"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_id_string_list


class DescribeVolumesRequest(TypedDict):
    volume_ids: NotRequired[
        "aws_sdk_ec2.types.volume_id_string_list.VolumeIdStringList"
    ]
    """<p>The volume IDs. If not specified, then all volumes are included in the response.</p>"""
    include_managed_resources: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to include managed resources in the output. If this parameter is set to <code>true</code>, the output includes resources that are managed by Amazon Web Services services, even if managed resource visibility is set to hidden.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>attachment.attach-time</code> - The time stamp when the attachment initiated.</p> </li> <li> <p> <code>attachment.delete-on-termination</code> - Whether the volume is deleted on instance termination.</p> </li> <li> <p> <code>attachment.device</code> - The device name specified in the block device mapping (for example, <code>/dev/sda1</code>).</p> </li> <li> <p> <code>attachment.instance-id</code> - The ID of the instance the volume is attached to.</p> </li> <li> <p> <code>attachment.status</code> - The attachment state (<code>attaching</code> | <code>attached</code> | <code>detaching</code>).</p> </li> <li> <p> <code>availability-zone</code> - The Availability Zone in which the volume was created.</p> </li> <li> <p> <code>availability-zone-id</code> - The ID of the Availability Zone in which the volume was created.</p> </li> <li> <p> <code>create-time</code> - The time stamp when the volume was created.</p> </li> <li> <p> <code>encrypted</code> - Indicates whether the volume is encrypted (<code>true</code> | <code>false</code>)</p> </li> <li> <p> <code>fast-restored</code> - Indicates whether the volume was created from a snapshot that is enabled for fast snapshot restore (<code>true</code> | <code>false</code>).</p> </li> <li> <p> <code>multi-attach-enabled</code> - Indicates whether the volume is enabled for Multi-Attach (<code>true</code> | <code>false</code>)</p> </li> <li> <p> <code>operator.managed</code> - A Boolean that indicates whether this is a managed volume.</p> </li> <li> <p> <code>operator.principal</code> - The principal that manages the volume. Only valid for managed volumes, where <code>managed</code> is <code>true</code>.</p> </li> <li> <p> <code>size</code> - The size of the volume, in GiB.</p> </li> <li> <p> <code>snapshot-id</code> - The snapshot from which the volume was created.</p> </li> <li> <p> <code>status</code> - The state of the volume (<code>creating</code> | <code>available</code> | <code>in-use</code> | <code>deleting</code> | <code>deleted</code> | <code>error</code>).</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>volume-id</code> - The volume ID.</p> </li> <li> <p> <code>volume-type</code> - The Amazon EBS volume type (<code>gp2</code> | <code>gp3</code> | <code>io1</code> | <code>io2</code> | <code>st1</code> | <code>sc1</code>| <code>standard</code>)</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    r"""<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVolumesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "volume_ids" in value:
        import aws_sdk_ec2.types.volume_id_string_list

        aws_sdk_ec2.types.volume_id_string_list.serialize_ec2_query(
            value["volume_ids"], pairs, f"{prefix}.VolumeIds"
        )
    if "include_managed_resources" in value:
        pairs.append(
            (
                f"{prefix}.IncludeManagedResources",
                "true" if value["include_managed_resources"] else "false",
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeVolumesRequest:
    out: DescribeVolumesRequest = {}  # type: ignore[typeddict-item]
    if el.find("VolumeIds") is not None:
        import aws_sdk_ec2.types.volume_id_string_list

        out["volume_ids"] = (
            aws_sdk_ec2.types.volume_id_string_list.deserialize_ec2_query(
                el, "VolumeIds"
            )
        )
    child_include_managed_resources = el.find("IncludeManagedResources")
    if child_include_managed_resources is not None:
        out["include_managed_resources"] = (
            child_include_managed_resources.text or ""
        ).lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
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
    return out
