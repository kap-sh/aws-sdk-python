"""Generated from Smithy shape ``com.amazonaws.workmail#ListGroupsFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.entity_state
    import capo_workmail.types.string


class ListGroupsFilters(TypedDict, closed=True):
    name_prefix: NotRequired["capo_workmail.types.string.String"]
    """<p>Filters only groups with the provided name prefix.</p>"""
    primary_email_prefix: NotRequired["capo_workmail.types.string.String"]
    """<p>Filters only groups with the provided primary email prefix.</p>"""
    state: NotRequired["capo_workmail.types.entity_state.EntityState"]
    """<p>Filters only groups with the provided state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGroupsFilters) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "primary_email_prefix" in value:
        out["PrimaryEmailPrefix"] = value["primary_email_prefix"]
    if "state" in value:
        import capo_workmail.types.entity_state

        out["State"] = capo_workmail.types.entity_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGroupsFilters:
    out: ListGroupsFilters = {}  # type: ignore[typeddict-item]
    if "NamePrefix" in data:
        out["name_prefix"] = data["NamePrefix"]
    if "PrimaryEmailPrefix" in data:
        out["primary_email_prefix"] = data["PrimaryEmailPrefix"]
    if "State" in data:
        import capo_workmail.types.entity_state

        out["state"] = capo_workmail.types.entity_state.deserialize_aws_json_1_1(
            data["State"]
        )
    return out
