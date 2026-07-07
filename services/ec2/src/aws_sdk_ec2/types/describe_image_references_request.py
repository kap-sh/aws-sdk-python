"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageReferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_image_references_image_id_string_list
    import aws_sdk_ec2.types.describe_image_references_max_results
    import aws_sdk_ec2.types.resource_type_request_list
    import aws_sdk_ec2.types.string


class DescribeImageReferencesRequest(TypedDict, closed=True):
    image_ids: NotRequired[
        "aws_sdk_ec2.types.describe_image_references_image_id_string_list.DescribeImageReferencesImageIdStringList"
    ]
    """<p>The IDs of the images to check for resource references.</p>"""
    include_all_resource_types: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    r"""<p>Specifies whether to check all supported Amazon Web Services resource types for image references. When specified, default values are applied for <code>ResourceTypeOptions</code>. For the default values, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-ami-references.html#how-ami-references-works\">How AMI reference checks work</a> in the <i>Amazon EC2 User Guide</i>. If you also specify <code>ResourceTypes</code> with <code>ResourceTypeOptions</code>, your specified values override the default values.</p> <p>Supported resource types: <code>ec2:Instance</code> | <code>ec2:LaunchTemplate</code> | <code>ssm:Parameter</code> | <code>imagebuilder:ImageRecipe</code> | <code>imagebuilder:ContainerRecipe</code> </p> <p>Either <code>IncludeAllResourceTypes</code> or <code>ResourceTypes</code> must be specified.</p>"""
    resource_types: NotRequired[
        "aws_sdk_ec2.types.resource_type_request_list.ResourceTypeRequestList"
    ]
    """<p>The Amazon Web Services resource types to check for image references.</p> <p>Either <code>IncludeAllResourceTypes</code> or <code>ResourceTypes</code> must be specified.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_image_references_max_results.DescribeImageReferencesMaxResults"
    ]
    r"""<p> The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeImageReferencesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_ids" in value:
        import aws_sdk_ec2.types.describe_image_references_image_id_string_list

        aws_sdk_ec2.types.describe_image_references_image_id_string_list.serialize_ec2_query(
            value["image_ids"], pairs, f"{prefix}.ImageIds"
        )
    if "include_all_resource_types" in value:
        pairs.append(
            (
                f"{prefix}.IncludeAllResourceTypes",
                "true" if value["include_all_resource_types"] else "false",
            )
        )
    if "resource_types" in value:
        import aws_sdk_ec2.types.resource_type_request_list

        aws_sdk_ec2.types.resource_type_request_list.serialize_ec2_query(
            value["resource_types"], pairs, f"{prefix}.ResourceTypes"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeImageReferencesRequest:
    out: DescribeImageReferencesRequest = {}  # type: ignore[typeddict-item]
    if el.find("ImageIds") is not None:
        import aws_sdk_ec2.types.describe_image_references_image_id_string_list

        out["image_ids"] = (
            aws_sdk_ec2.types.describe_image_references_image_id_string_list.deserialize_ec2_query(
                el, "ImageIds"
            )
        )
    child_include_all_resource_types = el.find("IncludeAllResourceTypes")
    if child_include_all_resource_types is not None:
        out["include_all_resource_types"] = (
            child_include_all_resource_types.text or ""
        ).lower() == "true"
    if el.find("ResourceTypes") is not None:
        import aws_sdk_ec2.types.resource_type_request_list

        out["resource_types"] = (
            aws_sdk_ec2.types.resource_type_request_list.deserialize_ec2_query(
                el, "ResourceTypes"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
