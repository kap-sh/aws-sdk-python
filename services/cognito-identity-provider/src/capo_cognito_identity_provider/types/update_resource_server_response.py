"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateResourceServerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.resource_server_type


class UpdateResourceServerResponse(TypedDict, closed=True):
    resource_server: (
        "capo_cognito_identity_provider.types.resource_server_type.ResourceServerType"
    )
    """<p>The updated details of the requested resource server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResourceServerResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.resource_server_type

    out["ResourceServer"] = (
        capo_cognito_identity_provider.types.resource_server_type.serialize_aws_json_1_1(
            value["resource_server"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResourceServerResponse:
    out: UpdateResourceServerResponse = {}  # type: ignore[typeddict-item]
    if "ResourceServer" in data:
        import capo_cognito_identity_provider.types.resource_server_type

        out["resource_server"] = (
            capo_cognito_identity_provider.types.resource_server_type.deserialize_aws_json_1_1(
                data["ResourceServer"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateResourceServerResponse.resource_server required"
        )
    return out
