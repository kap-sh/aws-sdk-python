"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateResourceServerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.resource_server_type


class CreateResourceServerResponse(TypedDict, closed=True):
    resource_server: "aws_sdk_cognito_identity_provider.types.resource_server_type.ResourceServerType"
    """<p>The details of the new resource server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResourceServerResponse) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.resource_server_type

    out["ResourceServer"] = (
        aws_sdk_cognito_identity_provider.types.resource_server_type.serialize_aws_json_1_1(
            value["resource_server"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResourceServerResponse:
    out: CreateResourceServerResponse = {}  # type: ignore[typeddict-item]
    if "ResourceServer" in data:
        import aws_sdk_cognito_identity_provider.types.resource_server_type

        out["resource_server"] = (
            aws_sdk_cognito_identity_provider.types.resource_server_type.deserialize_aws_json_1_1(
                data["ResourceServer"]
            )
        )
    else:
        raise DeserializationError(
            "CreateResourceServerResponse.resource_server required"
        )
    return out
