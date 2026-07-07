"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetServiceIndexOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.index_type


class GetServiceIndexOutput(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Resource Explorer index in the current Region.</p>"""
    type: NotRequired["aws_sdk_resource_explorer_2.types.index_type.IndexType"]
    """<p>The type of the index. Valid values are <code>LOCAL</code> (contains resources from the current Region only) or <code>AGGREGATOR</code> (contains replicated resource information from all Regions).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceIndexOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> GetServiceIndexOutput:
    out: GetServiceIndexOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
