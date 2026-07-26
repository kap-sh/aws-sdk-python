"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#DeleteIdentitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.unprocessed_identity_id_list


class DeleteIdentitiesResponse(TypedDict, closed=True):
    unprocessed_identity_ids: NotRequired[
        "capo_cognito_identity.types.unprocessed_identity_id_list.UnprocessedIdentityIdList"
    ]
    """<p>An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and IdentityId.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIdentitiesResponse) -> dict:
    out: dict = {}
    if "unprocessed_identity_ids" in value:
        import capo_cognito_identity.types.unprocessed_identity_id_list

        out["UnprocessedIdentityIds"] = (
            capo_cognito_identity.types.unprocessed_identity_id_list.serialize_aws_json_1_1(
                value["unprocessed_identity_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIdentitiesResponse:
    out: DeleteIdentitiesResponse = {}  # type: ignore[typeddict-item]
    if "UnprocessedIdentityIds" in data:
        import capo_cognito_identity.types.unprocessed_identity_id_list

        out["unprocessed_identity_ids"] = (
            capo_cognito_identity.types.unprocessed_identity_id_list.deserialize_aws_json_1_1(
                data["UnprocessedIdentityIds"]
            )
        )
    return out
