"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsEcrContainerAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.aws_ecr_container_sort_by
    import aws_sdk_inspector2.types.date_filter_list
    import aws_sdk_inspector2.types.number_filter_list
    import aws_sdk_inspector2.types.sort_order
    import aws_sdk_inspector2.types.string_filter_list


class AwsEcrContainerAggregation(TypedDict):
    resource_ids: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The container resource IDs.</p>"""
    image_shas: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The image SHA values.</p>"""
    repositories: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The container repositories.</p>"""
    architectures: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The architecture of the containers.</p>"""
    image_tags: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The image tags.</p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.sort_order.SortOrder"]
    """<p>The sort order (ascending or descending).</p>"""
    sort_by: NotRequired[
        "aws_sdk_inspector2.types.aws_ecr_container_sort_by.AwsEcrContainerSortBy"
    ]
    """<p>The value to sort by.</p>"""
    last_in_use_at: NotRequired[
        "aws_sdk_inspector2.types.date_filter_list.DateFilterList"
    ]
    """<p>The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.</p>"""
    in_use_count: NotRequired[
        "aws_sdk_inspector2.types.number_filter_list.NumberFilterList"
    ]
    """<p>The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcrContainerAggregation) -> dict:
    out: dict = {}
    if "resource_ids" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["resourceIds"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["resource_ids"]
        )
    if "image_shas" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["imageShas"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["image_shas"]
        )
    if "repositories" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["repositories"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["repositories"]
            )
        )
    if "architectures" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["architectures"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["architectures"]
            )
        )
    if "image_tags" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["imageTags"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["image_tags"]
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    if "last_in_use_at" in value:
        import aws_sdk_inspector2.types.date_filter_list

        out["lastInUseAt"] = aws_sdk_inspector2.types.date_filter_list.serialize_json(
            value["last_in_use_at"]
        )
    if "in_use_count" in value:
        import aws_sdk_inspector2.types.number_filter_list

        out["inUseCount"] = aws_sdk_inspector2.types.number_filter_list.serialize_json(
            value["in_use_count"]
        )
    return out


def deserialize_json(data: dict) -> AwsEcrContainerAggregation:
    out: AwsEcrContainerAggregation = {}  # type: ignore[typeddict-item]
    if "resourceIds" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["resource_ids"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["resourceIds"]
            )
        )
    if "imageShas" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["image_shas"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["imageShas"]
            )
        )
    if "repositories" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["repositories"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["repositories"]
            )
        )
    if "architectures" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["architectures"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["architectures"]
            )
        )
    if "imageTags" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["image_tags"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["imageTags"]
            )
        )
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    if "lastInUseAt" in data:
        import aws_sdk_inspector2.types.date_filter_list

        out["last_in_use_at"] = (
            aws_sdk_inspector2.types.date_filter_list.deserialize_json(
                data["lastInUseAt"]
            )
        )
    if "inUseCount" in data:
        import aws_sdk_inspector2.types.number_filter_list

        out["in_use_count"] = (
            aws_sdk_inspector2.types.number_filter_list.deserialize_json(
                data["inUseCount"]
            )
        )
    return out
