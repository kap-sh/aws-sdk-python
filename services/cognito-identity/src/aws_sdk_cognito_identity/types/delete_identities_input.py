"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#DeleteIdentitiesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_id_list


class DeleteIdentitiesInput(TypedDict):
    identity_ids_to_delete: (
        "aws_sdk_cognito_identity.types.identity_id_list.IdentityIdList"
    )
    """<p>A list of 1-60 identities that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIdentitiesInput) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity.types.identity_id_list

    out["IdentityIdsToDelete"] = (
        aws_sdk_cognito_identity.types.identity_id_list.serialize_aws_json_1_1(
            value["identity_ids_to_delete"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIdentitiesInput:
    out: DeleteIdentitiesInput = {}  # type: ignore[typeddict-item]
    if "IdentityIdsToDelete" in data:
        import aws_sdk_cognito_identity.types.identity_id_list

        out["identity_ids_to_delete"] = (
            aws_sdk_cognito_identity.types.identity_id_list.deserialize_aws_json_1_1(
                data["IdentityIdsToDelete"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteIdentitiesInput.identity_ids_to_delete required"
        )
    return out
