"""Generated from Smithy shape ``com.amazonaws.workmail#ListUsersFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.entity_state
    import aws_sdk_workmail.types.identity_provider_user_id_prefix
    import aws_sdk_workmail.types.string
    import aws_sdk_workmail.types.user_attribute


class ListUsersFilters(TypedDict):
    username_prefix: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>Filters only users with the provided username prefix.</p>"""
    display_name_prefix: NotRequired[
        "aws_sdk_workmail.types.user_attribute.UserAttribute"
    ]
    """<p>Filters only users with the provided display name prefix.</p>"""
    primary_email_prefix: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>Filters only users with the provided email prefix.</p>"""
    state: NotRequired["aws_sdk_workmail.types.entity_state.EntityState"]
    """<p>Filters only users with the provided state.</p>"""
    identity_provider_user_id_prefix: NotRequired[
        "aws_sdk_workmail.types.identity_provider_user_id_prefix.IdentityProviderUserIdPrefix"
    ]
    """<p>Filters only users with the ID from the IAM Identity Center.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsersFilters) -> dict:
    out: dict = {}
    if "username_prefix" in value:
        out["UsernamePrefix"] = value["username_prefix"]
    if "display_name_prefix" in value:
        out["DisplayNamePrefix"] = value["display_name_prefix"]
    if "primary_email_prefix" in value:
        out["PrimaryEmailPrefix"] = value["primary_email_prefix"]
    if "state" in value:
        import aws_sdk_workmail.types.entity_state

        out["State"] = aws_sdk_workmail.types.entity_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "identity_provider_user_id_prefix" in value:
        out["IdentityProviderUserIdPrefix"] = value["identity_provider_user_id_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsersFilters:
    out: ListUsersFilters = {}  # type: ignore[typeddict-item]
    if "UsernamePrefix" in data:
        out["username_prefix"] = data["UsernamePrefix"]
    if "DisplayNamePrefix" in data:
        out["display_name_prefix"] = data["DisplayNamePrefix"]
    if "PrimaryEmailPrefix" in data:
        out["primary_email_prefix"] = data["PrimaryEmailPrefix"]
    if "State" in data:
        import aws_sdk_workmail.types.entity_state

        out["state"] = aws_sdk_workmail.types.entity_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "IdentityProviderUserIdPrefix" in data:
        out["identity_provider_user_id_prefix"] = data["IdentityProviderUserIdPrefix"]
    return out
