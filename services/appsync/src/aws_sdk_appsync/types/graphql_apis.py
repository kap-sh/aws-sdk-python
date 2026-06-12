"""Generated from Smithy shape ``com.amazonaws.appsync#GraphqlApis``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.graphql_api

GraphqlApis: TypeAlias = list["aws_sdk_appsync.types.graphql_api.GraphqlApi"]


# --- restJson1 ser/de ---
def serialize_json(value: GraphqlApis) -> list:
    import aws_sdk_appsync.types.graphql_api

    out: list = []
    for item in value:
        out.append(aws_sdk_appsync.types.graphql_api.serialize_json(item))
    return out


def deserialize_json(data: list) -> GraphqlApis:
    import aws_sdk_appsync.types.graphql_api

    out: GraphqlApis = []
    for item in data:
        out.append(aws_sdk_appsync.types.graphql_api.deserialize_json(item))
    return out
