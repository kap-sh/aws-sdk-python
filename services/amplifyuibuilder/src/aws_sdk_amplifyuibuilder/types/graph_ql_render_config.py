"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GraphQLRenderConfig``."""

from typing_extensions import TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError


class GraphQLRenderConfig(TypedDict, closed=True):
    types_file_path: "str"
    """<p>The path to the GraphQL types file, relative to the component output directory.</p>"""
    queries_file_path: "str"
    """<p>The path to the GraphQL queries file, relative to the component output directory.</p>"""
    mutations_file_path: "str"
    """<p>The path to the GraphQL mutations file, relative to the component output directory.</p>"""
    subscriptions_file_path: "str"
    """<p>The path to the GraphQL subscriptions file, relative to the component output directory.</p>"""
    fragments_file_path: "str"
    """<p>The path to the GraphQL fragments file, relative to the component output directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GraphQLRenderConfig) -> dict:
    out: dict = {}
    out["typesFilePath"] = value["types_file_path"]
    out["queriesFilePath"] = value["queries_file_path"]
    out["mutationsFilePath"] = value["mutations_file_path"]
    out["subscriptionsFilePath"] = value["subscriptions_file_path"]
    out["fragmentsFilePath"] = value["fragments_file_path"]
    return out


def deserialize_json(data: dict) -> GraphQLRenderConfig:
    out: GraphQLRenderConfig = {}  # type: ignore[typeddict-item]
    if "typesFilePath" in data:
        out["types_file_path"] = data["typesFilePath"]
    else:
        raise DeserializationError("GraphQLRenderConfig.types_file_path required")
    if "queriesFilePath" in data:
        out["queries_file_path"] = data["queriesFilePath"]
    else:
        raise DeserializationError("GraphQLRenderConfig.queries_file_path required")
    if "mutationsFilePath" in data:
        out["mutations_file_path"] = data["mutationsFilePath"]
    else:
        raise DeserializationError("GraphQLRenderConfig.mutations_file_path required")
    if "subscriptionsFilePath" in data:
        out["subscriptions_file_path"] = data["subscriptionsFilePath"]
    else:
        raise DeserializationError(
            "GraphQLRenderConfig.subscriptions_file_path required"
        )
    if "fragmentsFilePath" in data:
        out["fragments_file_path"] = data["fragmentsFilePath"]
    else:
        raise DeserializationError("GraphQLRenderConfig.fragments_file_path required")
    return out
