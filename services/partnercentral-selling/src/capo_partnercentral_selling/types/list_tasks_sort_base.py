"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListTasksSortBase``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.list_tasks_sort_name
    import capo_partnercentral_selling.types.sort_order


class ListTasksSortBase(TypedDict, closed=True):
    sort_order: "capo_partnercentral_selling.types.sort_order.SortOrder"
    """<p> Determines the order in which the sorted results are presented. </p>"""
    sort_by: "capo_partnercentral_selling.types.list_tasks_sort_name.ListTasksSortName"
    """<p> Specifies the field by which the task list should be sorted. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTasksSortBase) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.sort_order

    out["SortOrder"] = (
        capo_partnercentral_selling.types.sort_order.serialize_aws_json_1_0(
            value["sort_order"]
        )
    )
    import capo_partnercentral_selling.types.list_tasks_sort_name

    out["SortBy"] = (
        capo_partnercentral_selling.types.list_tasks_sort_name.serialize_aws_json_1_0(
            value["sort_by"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTasksSortBase:
    out: ListTasksSortBase = {}  # type: ignore[typeddict-item]
    if "SortOrder" in data:
        import capo_partnercentral_selling.types.sort_order

        out["sort_order"] = (
            capo_partnercentral_selling.types.sort_order.deserialize_aws_json_1_0(
                data["SortOrder"]
            )
        )
    else:
        raise DeserializationError("ListTasksSortBase.sort_order required")
    if "SortBy" in data:
        import capo_partnercentral_selling.types.list_tasks_sort_name

        out["sort_by"] = (
            capo_partnercentral_selling.types.list_tasks_sort_name.deserialize_aws_json_1_0(
                data["SortBy"]
            )
        )
    else:
        raise DeserializationError("ListTasksSortBase.sort_by required")
    return out
