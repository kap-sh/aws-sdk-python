"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeTagsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.tag_key_list
    import aws_sdk_redshift.types.tag_value_list


class DescribeTagsMessage(TypedDict, closed=True):
    resource_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for which you want to describe the tag or tags. For example, <code>arn:aws:redshift:us-east-2:123456789:cluster:t1</code>. </p>"""
    resource_type: NotRequired["aws_sdk_redshift.types.string.String"]
    r"""<p>The type of resource with which you want to view tags. Valid resource types are: </p> <ul> <li> <p>Cluster</p> </li> <li> <p>CIDR/IP</p> </li> <li> <p>EC2 security group</p> </li> <li> <p>Snapshot</p> </li> <li> <p>Cluster security group</p> </li> <li> <p>Subnet group</p> </li> <li> <p>HSM connection</p> </li> <li> <p>HSM certificate</p> </li> <li> <p>Parameter group</p> </li> <li> <p>Snapshot copy grant</p> </li> <li> <p>Integration (zero-ETL integration or S3 event integration)</p> <note> <p>To describe the tags associated with an <code>integration</code>, don't specify <code>ResourceType</code>, instead specify the <code>ResourceName</code> of the integration.</p> </note> </li> </ul> <p>For more information about Amazon Redshift resource types and constructing ARNs, go to <a href=\"https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-iam-access-control-specify-actions\">Specifying Policy Elements: Actions, Effects, Resources, and Principals</a> in the Amazon Redshift Cluster Management Guide. </p>"""
    max_records: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned <code>marker</code> value. </p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>marker</code> parameter and retrying the command. If the <code>marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    tag_keys: NotRequired["aws_sdk_redshift.types.tag_key_list.TagKeyList"]
    """<p>A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.</p>"""
    tag_values: NotRequired["aws_sdk_redshift.types.tag_value_list.TagValueList"]
    """<p>A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTagsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_name" in value:
        pairs.append((f"{prefix}.ResourceName", str(value["resource_name"])))
    if "resource_type" in value:
        pairs.append((f"{prefix}.ResourceType", str(value["resource_type"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "tag_keys" in value:
        import aws_sdk_redshift.types.tag_key_list

        aws_sdk_redshift.types.tag_key_list.serialize_query(
            value["tag_keys"], pairs, f"{prefix}.TagKeys"
        )
    if "tag_values" in value:
        import aws_sdk_redshift.types.tag_value_list

        aws_sdk_redshift.types.tag_value_list.serialize_query(
            value["tag_values"], pairs, f"{prefix}.TagValues"
        )


def deserialize_query(el: Element) -> DescribeTagsMessage:
    out: DescribeTagsMessage = {}  # type: ignore[typeddict-item]
    child_resource_name = el.find("ResourceName")
    if child_resource_name is not None:
        out["resource_name"] = str(child_resource_name.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import aws_sdk_redshift.types.tag_key_list

        out["tag_keys"] = aws_sdk_redshift.types.tag_key_list.deserialize_query(
            child_tag_keys
        )
    child_tag_values = el.find("TagValues")
    if child_tag_values is not None:
        import aws_sdk_redshift.types.tag_value_list

        out["tag_values"] = aws_sdk_redshift.types.tag_value_list.deserialize_query(
            child_tag_values
        )
    return out
