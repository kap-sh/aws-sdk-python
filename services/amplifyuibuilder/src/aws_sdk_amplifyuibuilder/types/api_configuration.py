"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ApiConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.data_store_render_config
    import aws_sdk_amplifyuibuilder.types.graph_ql_render_config
    import aws_sdk_amplifyuibuilder.types.no_api_render_config


class _ApiConfiguration_graphQLConfig(TypedDict, closed=True):
    graphQLConfig: (
        "aws_sdk_amplifyuibuilder.types.graph_ql_render_config.GraphQLRenderConfig"
    )


class _ApiConfiguration_dataStoreConfig(TypedDict, closed=True):
    dataStoreConfig: (
        "aws_sdk_amplifyuibuilder.types.data_store_render_config.DataStoreRenderConfig"
    )


class _ApiConfiguration_noApiConfig(TypedDict, closed=True):
    noApiConfig: "aws_sdk_amplifyuibuilder.types.no_api_render_config.NoApiRenderConfig"


ApiConfiguration: TypeAlias = (
    _ApiConfiguration_graphQLConfig
    | _ApiConfiguration_dataStoreConfig
    | _ApiConfiguration_noApiConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: ApiConfiguration) -> dict:
    if "graphQLConfig" in value:
        import aws_sdk_amplifyuibuilder.types.graph_ql_render_config

        return {
            "graphQLConfig": aws_sdk_amplifyuibuilder.types.graph_ql_render_config.serialize_json(
                value["graphQLConfig"]
            )
        }
    elif "dataStoreConfig" in value:
        import aws_sdk_amplifyuibuilder.types.data_store_render_config

        return {
            "dataStoreConfig": aws_sdk_amplifyuibuilder.types.data_store_render_config.serialize_json(
                value["dataStoreConfig"]
            )
        }
    elif "noApiConfig" in value:
        import aws_sdk_amplifyuibuilder.types.no_api_render_config

        return {
            "noApiConfig": aws_sdk_amplifyuibuilder.types.no_api_render_config.serialize_json(
                value["noApiConfig"]
            )
        }
    else:
        raise SerializationError("ApiConfiguration: no variant present")


def deserialize_json(data: dict) -> ApiConfiguration:
    if "graphQLConfig" in data:
        import aws_sdk_amplifyuibuilder.types.graph_ql_render_config

        return {
            "graphQLConfig": aws_sdk_amplifyuibuilder.types.graph_ql_render_config.deserialize_json(
                data["graphQLConfig"]
            )
        }
    elif "dataStoreConfig" in data:
        import aws_sdk_amplifyuibuilder.types.data_store_render_config

        return {
            "dataStoreConfig": aws_sdk_amplifyuibuilder.types.data_store_render_config.deserialize_json(
                data["dataStoreConfig"]
            )
        }
    elif "noApiConfig" in data:
        import aws_sdk_amplifyuibuilder.types.no_api_render_config

        return {
            "noApiConfig": aws_sdk_amplifyuibuilder.types.no_api_render_config.deserialize_json(
                data["noApiConfig"]
            )
        }
    else:
        raise DeserializationError("ApiConfiguration: no recognized variant key")
