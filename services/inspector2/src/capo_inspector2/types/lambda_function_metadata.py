"""Generated from Smithy shape ``com.amazonaws.inspector2#LambdaFunctionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.lambda_layer_list
    import capo_inspector2.types.runtime
    import capo_inspector2.types.tag_map


class LambdaFunctionMetadata(TypedDict, closed=True):
    function_tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The resource tags on an Amazon Web Services Lambda function.</p>"""
    layers: NotRequired["capo_inspector2.types.lambda_layer_list.LambdaLayerList"]
    """<p>The layers for an Amazon Web Services Lambda function. A Lambda function can have up to five layers.</p>"""
    function_name: NotRequired["str"]
    """<p>The name of a function.</p>"""
    runtime: NotRequired["capo_inspector2.types.runtime.Runtime"]
    """<p>An Amazon Web Services Lambda function's runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaFunctionMetadata) -> dict:
    out: dict = {}
    if "function_tags" in value:
        import capo_inspector2.types.tag_map

        out["functionTags"] = capo_inspector2.types.tag_map.serialize_json(
            value["function_tags"]
        )
    if "layers" in value:
        import capo_inspector2.types.lambda_layer_list

        out["layers"] = capo_inspector2.types.lambda_layer_list.serialize_json(
            value["layers"]
        )
    if "function_name" in value:
        out["functionName"] = value["function_name"]
    if "runtime" in value:
        out["runtime"] = value["runtime"]
    return out


def deserialize_json(data: dict) -> LambdaFunctionMetadata:
    out: LambdaFunctionMetadata = {}  # type: ignore[typeddict-item]
    if "functionTags" in data:
        import capo_inspector2.types.tag_map

        out["function_tags"] = capo_inspector2.types.tag_map.deserialize_json(
            data["functionTags"]
        )
    if "layers" in data:
        import capo_inspector2.types.lambda_layer_list

        out["layers"] = capo_inspector2.types.lambda_layer_list.deserialize_json(
            data["layers"]
        )
    if "functionName" in data:
        out["function_name"] = data["functionName"]
    if "runtime" in data:
        out["runtime"] = data["runtime"]
    return out
