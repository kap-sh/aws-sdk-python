"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsEcrContainerAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.aws_ecr_container_sort_by
    import capo_inspector2.types.date_filter_list
    import capo_inspector2.types.number_filter_list
    import capo_inspector2.types.sort_order
    import capo_inspector2.types.string_filter_list


class AwsEcrContainerAggregation(TypedDict, closed=True):
    resource_ids: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The container resource IDs.</p>"""
    image_shas: NotRequired["capo_inspector2.types.string_filter_list.StringFilterList"]
    """<p>The image SHA values.</p>"""
    repositories: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The container repositories.</p>"""
    architectures: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The architecture of the containers.</p>"""
    image_tags: NotRequired["capo_inspector2.types.string_filter_list.StringFilterList"]
    """<p>The image tags.</p>"""
    sort_order: NotRequired["capo_inspector2.types.sort_order.SortOrder"]
    """<p>The sort order (ascending or descending).</p>"""
    sort_by: NotRequired[
        "capo_inspector2.types.aws_ecr_container_sort_by.AwsEcrContainerSortBy"
    ]
    """<p>The value to sort by.</p>"""
    last_in_use_at: NotRequired["capo_inspector2.types.date_filter_list.DateFilterList"]
    """<p>The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.</p>"""
    in_use_count: NotRequired[
        "capo_inspector2.types.number_filter_list.NumberFilterList"
    ]
    """<p>The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcrContainerAggregation) -> dict:
    out: dict = {}
    if "resource_ids" in value:
        import capo_inspector2.types.string_filter_list

        out["resourceIds"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["resource_ids"]
        )
    if "image_shas" in value:
        import capo_inspector2.types.string_filter_list

        out["imageShas"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["image_shas"]
        )
    if "repositories" in value:
        import capo_inspector2.types.string_filter_list

        out["repositories"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["repositories"]
        )
    if "architectures" in value:
        import capo_inspector2.types.string_filter_list

        out["architectures"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["architectures"]
        )
    if "image_tags" in value:
        import capo_inspector2.types.string_filter_list

        out["imageTags"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["image_tags"]
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    if "last_in_use_at" in value:
        import capo_inspector2.types.date_filter_list

        out["lastInUseAt"] = capo_inspector2.types.date_filter_list.serialize_json(
            value["last_in_use_at"]
        )
    if "in_use_count" in value:
        import capo_inspector2.types.number_filter_list

        out["inUseCount"] = capo_inspector2.types.number_filter_list.serialize_json(
            value["in_use_count"]
        )
    return out


def deserialize_json(data: dict) -> AwsEcrContainerAggregation:
    out: AwsEcrContainerAggregation = {}  # type: ignore[typeddict-item]
    if "resourceIds" in data:
        import capo_inspector2.types.string_filter_list

        out["resource_ids"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["resourceIds"]
        )
    if "imageShas" in data:
        import capo_inspector2.types.string_filter_list

        out["image_shas"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["imageShas"]
        )
    if "repositories" in data:
        import capo_inspector2.types.string_filter_list

        out["repositories"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["repositories"]
        )
    if "architectures" in data:
        import capo_inspector2.types.string_filter_list

        out["architectures"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["architectures"]
            )
        )
    if "imageTags" in data:
        import capo_inspector2.types.string_filter_list

        out["image_tags"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["imageTags"]
        )
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    if "lastInUseAt" in data:
        import capo_inspector2.types.date_filter_list

        out["last_in_use_at"] = capo_inspector2.types.date_filter_list.deserialize_json(
            data["lastInUseAt"]
        )
    if "inUseCount" in data:
        import capo_inspector2.types.number_filter_list

        out["in_use_count"] = capo_inspector2.types.number_filter_list.deserialize_json(
            data["inUseCount"]
        )
    return out
