"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListResourceServersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.pagination_key_type
    import aws_sdk_cognito_identity_provider.types.resource_servers_list_type


class ListResourceServersResponse(TypedDict):
    resource_servers: "aws_sdk_cognito_identity_provider.types.resource_servers_list_type.ResourceServersListType"
    """<p>An array of resource servers and the details of their configuration. For each, the response includes names, identifiers, and custom scopes.</p>"""
    next_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.pagination_key_type.PaginationKeyType"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceServersResponse) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.resource_servers_list_type

    out["ResourceServers"] = (
        aws_sdk_cognito_identity_provider.types.resource_servers_list_type.serialize_aws_json_1_1(
            value["resource_servers"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceServersResponse:
    out: ListResourceServersResponse = {}  # type: ignore[typeddict-item]
    if "ResourceServers" in data:
        import aws_sdk_cognito_identity_provider.types.resource_servers_list_type

        out["resource_servers"] = (
            aws_sdk_cognito_identity_provider.types.resource_servers_list_type.deserialize_aws_json_1_1(
                data["ResourceServers"]
            )
        )
    else:
        raise DeserializationError(
            "ListResourceServersResponse.resource_servers required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
