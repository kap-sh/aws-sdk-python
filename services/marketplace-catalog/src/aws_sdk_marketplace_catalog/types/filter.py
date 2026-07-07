"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.filter_name
    import aws_sdk_marketplace_catalog.types.value_list


class Filter(TypedDict, closed=True):
    name: NotRequired["aws_sdk_marketplace_catalog.types.filter_name.FilterName"]
    """<p>For <code>ListEntities</code>, the supported value for this is an <code>EntityId</code>.</p> <p>For <code>ListChangeSets</code>, the supported values are as follows:</p>"""
    value_list: NotRequired["aws_sdk_marketplace_catalog.types.value_list.ValueList"]
    """<p> <code>ListEntities</code> - This is a list of unique <code>EntityId</code>s.</p> <p> <code>ListChangeSets</code> - The supported filter names and associated <code>ValueList</code>s is as follows:</p> <ul> <li> <p> <code>ChangeSetName</code> - The supported <code>ValueList</code> is a list of non-unique <code>ChangeSetName</code>s. These are defined when you call the <code>StartChangeSet</code> action.</p> </li> <li> <p> <code>Status</code> - The supported <code>ValueList</code> is a list of statuses for all change set requests.</p> </li> <li> <p> <code>EntityId</code> - The supported <code>ValueList</code> is a list of unique <code>EntityId</code>s.</p> </li> <li> <p> <code>BeforeStartTime</code> - The supported <code>ValueList</code> is a list of all change sets that started before the filter value.</p> </li> <li> <p> <code>AfterStartTime</code> - The supported <code>ValueList</code> is a list of all change sets that started after the filter value.</p> </li> <li> <p> <code>BeforeEndTime</code> - The supported <code>ValueList</code> is a list of all change sets that ended before the filter value.</p> </li> <li> <p> <code>AfterEndTime</code> - The supported <code>ValueList</code> is a list of all change sets that ended after the filter value.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.value_list

        out["ValueList"] = aws_sdk_marketplace_catalog.types.value_list.serialize_json(
            value["value_list"]
        )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
