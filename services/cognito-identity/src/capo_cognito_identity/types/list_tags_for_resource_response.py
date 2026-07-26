"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_pool_tags_type


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired[
        "capo_cognito_identity.types.identity_pool_tags_type.IdentityPoolTagsType"
    ]
    """<p>The tags that are assigned to the identity pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_cognito_identity.types.identity_pool_tags_type

        out["Tags"] = (
            capo_cognito_identity.types.identity_pool_tags_type.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_cognito_identity.types.identity_pool_tags_type

        out["tags"] = (
            capo_cognito_identity.types.identity_pool_tags_type.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    return out
