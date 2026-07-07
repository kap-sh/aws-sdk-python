"""Generated from Smithy shape ``com.amazonaws.workmail#ListGroupsForEntityFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.string


class ListGroupsForEntityFilters(TypedDict, closed=True):
    group_name_prefix: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>Filters only group names that start with the provided name prefix.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGroupsForEntityFilters) -> dict:
    out: dict = {}
    if "group_name_prefix" in value:
        out["GroupNamePrefix"] = value["group_name_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGroupsForEntityFilters:
    out: ListGroupsForEntityFilters = {}  # type: ignore[typeddict-item]
    if "GroupNamePrefix" in data:
        out["group_name_prefix"] = data["GroupNamePrefix"]
    return out
