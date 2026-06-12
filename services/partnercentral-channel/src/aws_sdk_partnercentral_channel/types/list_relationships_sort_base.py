"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListRelationshipsSortBase``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.list_relationships_sort_name
    import aws_sdk_partnercentral_channel.types.sort_order


class ListRelationshipsSortBase(TypedDict):
    sort_order: "aws_sdk_partnercentral_channel.types.sort_order.SortOrder"
    """<p>The sort order (ascending or descending).</p>"""
    sort_by: "aws_sdk_partnercentral_channel.types.list_relationships_sort_name.ListRelationshipsSortName"
    """<p>The field to sort by.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRelationshipsSortBase) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_channel.types.sort_order

    out["sortOrder"] = (
        aws_sdk_partnercentral_channel.types.sort_order.serialize_aws_json_1_0(
            value["sort_order"]
        )
    )
    import aws_sdk_partnercentral_channel.types.list_relationships_sort_name

    out["sortBy"] = (
        aws_sdk_partnercentral_channel.types.list_relationships_sort_name.serialize_aws_json_1_0(
            value["sort_by"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRelationshipsSortBase:
    out: ListRelationshipsSortBase = {}  # type: ignore[typeddict-item]
    if "sortOrder" in data:
        import aws_sdk_partnercentral_channel.types.sort_order

        out["sort_order"] = (
            aws_sdk_partnercentral_channel.types.sort_order.deserialize_aws_json_1_0(
                data["sortOrder"]
            )
        )
    else:
        raise DeserializationError("ListRelationshipsSortBase.sort_order required")
    if "sortBy" in data:
        import aws_sdk_partnercentral_channel.types.list_relationships_sort_name

        out["sort_by"] = (
            aws_sdk_partnercentral_channel.types.list_relationships_sort_name.deserialize_aws_json_1_0(
                data["sortBy"]
            )
        )
    else:
        raise DeserializationError("ListRelationshipsSortBase.sort_by required")
    return out
