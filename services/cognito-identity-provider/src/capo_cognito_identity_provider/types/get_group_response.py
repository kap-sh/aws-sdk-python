"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.group_type


class GetGroupResponse(TypedDict, closed=True):
    group: NotRequired["capo_cognito_identity_provider.types.group_type.GroupType"]
    """<p>A container for the requested group. Includes description, precedence, and IAM role values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGroupResponse) -> dict:
    out: dict = {}
    if "group" in value:
        import capo_cognito_identity_provider.types.group_type

        out["Group"] = (
            capo_cognito_identity_provider.types.group_type.serialize_aws_json_1_1(
                value["group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGroupResponse:
    out: GetGroupResponse = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import capo_cognito_identity_provider.types.group_type

        out["group"] = (
            capo_cognito_identity_provider.types.group_type.deserialize_aws_json_1_1(
                data["Group"]
            )
        )
    return out
