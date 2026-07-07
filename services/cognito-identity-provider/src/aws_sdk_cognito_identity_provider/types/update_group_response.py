"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.group_type


class UpdateGroupResponse(TypedDict, closed=True):
    group: NotRequired["aws_sdk_cognito_identity_provider.types.group_type.GroupType"]
    """<p>Contains the updated details of the group, including precedence, IAM role, and description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGroupResponse) -> dict:
    out: dict = {}
    if "group" in value:
        import aws_sdk_cognito_identity_provider.types.group_type

        out["Group"] = (
            aws_sdk_cognito_identity_provider.types.group_type.serialize_aws_json_1_1(
                value["group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGroupResponse:
    out: UpdateGroupResponse = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import aws_sdk_cognito_identity_provider.types.group_type

        out["group"] = (
            aws_sdk_cognito_identity_provider.types.group_type.deserialize_aws_json_1_1(
                data["Group"]
            )
        )
    return out
