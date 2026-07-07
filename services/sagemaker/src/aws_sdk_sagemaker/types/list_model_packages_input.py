"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelPackagesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.arn_or_name
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.model_approval_status
    import aws_sdk_sagemaker.types.model_package_sort_by
    import aws_sdk_sagemaker.types.model_package_type
    import aws_sdk_sagemaker.types.name_contains
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order


class ListModelPackagesInput(TypedDict, closed=True):
    creation_time_after: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>A filter that returns only model packages created after the specified time (timestamp).</p>"""
    creation_time_before: NotRequired[
        "aws_sdk_sagemaker.types.creation_time.CreationTime"
    ]
    """<p>A filter that returns only model packages created before the specified time (timestamp).</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of model packages to return in the response.</p>"""
    name_contains: NotRequired["aws_sdk_sagemaker.types.name_contains.NameContains"]
    """<p>A string in the model package name. This filter returns only model packages whose name contains the specified string.</p>"""
    model_approval_status: NotRequired[
        "aws_sdk_sagemaker.types.model_approval_status.ModelApprovalStatus"
    ]
    """<p>A filter that returns only the model packages with the specified approval status.</p>"""
    model_package_group_name: NotRequired[
        "aws_sdk_sagemaker.types.arn_or_name.ArnOrName"
    ]
    """<p>A filter that returns only model versions that belong to the specified model group.</p>"""
    model_package_type: NotRequired[
        "aws_sdk_sagemaker.types.model_package_type.ModelPackageType"
    ]
    """<p>A filter that returns only the model packages of the specified type. This can be one of the following values.</p> <ul> <li> <p> <code>UNVERSIONED</code> - List only unversioined models. This is the default value if no <code>ModelPackageType</code> is specified.</p> </li> <li> <p> <code>VERSIONED</code> - List only versioned models.</p> </li> <li> <p> <code>BOTH</code> - List both versioned and unversioned models.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response to a previous <code>ListModelPackages</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of model packages, use the token in the next request.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.model_package_sort_by.ModelPackageSortBy"
    ]
    """<p>The parameter by which to sort the results. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for the results. The default is <code>Ascending</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelPackagesInput) -> dict:
    out: dict = {}
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "model_approval_status" in value:
        import aws_sdk_sagemaker.types.model_approval_status

        out["ModelApprovalStatus"] = (
            aws_sdk_sagemaker.types.model_approval_status.serialize_aws_json_1_1(
                value["model_approval_status"]
            )
        )
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    if "model_package_type" in value:
        import aws_sdk_sagemaker.types.model_package_type

        out["ModelPackageType"] = (
            aws_sdk_sagemaker.types.model_package_type.serialize_aws_json_1_1(
                value["model_package_type"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.model_package_sort_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.model_package_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelPackagesInput:
    out: ListModelPackagesInput = {}  # type: ignore[typeddict-item]
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "ModelApprovalStatus" in data:
        import aws_sdk_sagemaker.types.model_approval_status

        out["model_approval_status"] = (
            aws_sdk_sagemaker.types.model_approval_status.deserialize_aws_json_1_1(
                data["ModelApprovalStatus"]
            )
        )
    if "ModelPackageGroupName" in data:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    if "ModelPackageType" in data:
        import aws_sdk_sagemaker.types.model_package_type

        out["model_package_type"] = (
            aws_sdk_sagemaker.types.model_package_type.deserialize_aws_json_1_1(
                data["ModelPackageType"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.model_package_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.model_package_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    return out
