"""Generated from Smithy shape ``com.amazonaws.workmail#ListResourcesFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.entity_state
    import aws_sdk_workmail.types.string


class ListResourcesFilters(TypedDict, closed=True):
    name_prefix: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>Filters only resource that start with the entered name prefix .</p>"""
    primary_email_prefix: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>Filters only resource with the provided primary email prefix.</p>"""
    state: NotRequired["aws_sdk_workmail.types.entity_state.EntityState"]
    """<p>Filters only resource with the provided state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesFilters) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "primary_email_prefix" in value:
        out["PrimaryEmailPrefix"] = value["primary_email_prefix"]
    if "state" in value:
        import aws_sdk_workmail.types.entity_state

        out["State"] = aws_sdk_workmail.types.entity_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesFilters:
    out: ListResourcesFilters = {}  # type: ignore[typeddict-item]
    if "NamePrefix" in data:
        out["name_prefix"] = data["NamePrefix"]
    if "PrimaryEmailPrefix" in data:
        out["primary_email_prefix"] = data["PrimaryEmailPrefix"]
    if "State" in data:
        import aws_sdk_workmail.types.entity_state

        out["state"] = aws_sdk_workmail.types.entity_state.deserialize_aws_json_1_1(
            data["State"]
        )
    return out
