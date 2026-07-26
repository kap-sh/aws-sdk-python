"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.group_type


class CreateGroupResponse(TypedDict, closed=True):
    group: NotRequired["capo_cognito_identity_provider.types.group_type.GroupType"]
    """<p>The response object for a created group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGroupResponse) -> dict:
    out: dict = {}
    if "group" in value:
        import capo_cognito_identity_provider.types.group_type

        out["Group"] = (
            capo_cognito_identity_provider.types.group_type.serialize_aws_json_1_1(
                value["group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGroupResponse:
    out: CreateGroupResponse = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import capo_cognito_identity_provider.types.group_type

        out["group"] = (
            capo_cognito_identity_provider.types.group_type.deserialize_aws_json_1_1(
                data["Group"]
            )
        )
    return out
