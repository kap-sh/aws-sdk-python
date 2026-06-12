"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementSort``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.engagement_sort_name
    import aws_sdk_partnercentral_selling.types.sort_order


class EngagementSort(TypedDict):
    sort_order: "aws_sdk_partnercentral_selling.types.sort_order.SortOrder"
    """<p>The order in which to sort the results.</p>"""
    sort_by: (
        "aws_sdk_partnercentral_selling.types.engagement_sort_name.EngagementSortName"
    )
    """<p>The field by which to sort the results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementSort) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_selling.types.sort_order

    out["SortOrder"] = (
        aws_sdk_partnercentral_selling.types.sort_order.serialize_aws_json_1_0(
            value["sort_order"]
        )
    )
    import aws_sdk_partnercentral_selling.types.engagement_sort_name

    out["SortBy"] = (
        aws_sdk_partnercentral_selling.types.engagement_sort_name.serialize_aws_json_1_0(
            value["sort_by"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EngagementSort:
    out: EngagementSort = {}  # type: ignore[typeddict-item]
    if "SortOrder" in data:
        import aws_sdk_partnercentral_selling.types.sort_order

        out["sort_order"] = (
            aws_sdk_partnercentral_selling.types.sort_order.deserialize_aws_json_1_0(
                data["SortOrder"]
            )
        )
    else:
        raise DeserializationError("EngagementSort.sort_order required")
    if "SortBy" in data:
        import aws_sdk_partnercentral_selling.types.engagement_sort_name

        out["sort_by"] = (
            aws_sdk_partnercentral_selling.types.engagement_sort_name.deserialize_aws_json_1_0(
                data["SortBy"]
            )
        )
    else:
        raise DeserializationError("EngagementSort.sort_by required")
    return out
