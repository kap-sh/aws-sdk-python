"""Generated from Smithy shape ``com.amazonaws.novaact#ModelAlias``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.model_id


class ModelAlias(TypedDict):
    alias_name: "aws_sdk_nova_act.types.model_id.ModelId"
    """<p>The name of the model alias.</p>"""
    latest_model_id: "aws_sdk_nova_act.types.model_id.ModelId"
    """<p>The model ID that this alias currently points to.</p>"""
    resolved_model_id: NotRequired["aws_sdk_nova_act.types.model_id.ModelId"]
    """<p>The resolved model ID after alias resolution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelAlias) -> dict:
    out: dict = {}
    out["aliasName"] = value["alias_name"]
    out["latestModelId"] = value["latest_model_id"]
    if "resolved_model_id" in value:
        out["resolvedModelId"] = value["resolved_model_id"]
    return out


def deserialize_json(data: dict) -> ModelAlias:
    out: ModelAlias = {}  # type: ignore[typeddict-item]
    if "aliasName" in data:
        out["alias_name"] = data["aliasName"]
    else:
        raise DeserializationError("ModelAlias.alias_name required")
    if "latestModelId" in data:
        out["latest_model_id"] = data["latestModelId"]
    else:
        raise DeserializationError("ModelAlias.latest_model_id required")
    if "resolvedModelId" in data:
        out["resolved_model_id"] = data["resolvedModelId"]
    return out
