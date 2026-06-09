"""Generated from Smithy shape ``com.amazonaws.kms#ListAliasesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.alias_list
    import aws_sdk_kms.types.boolean_type
    import aws_sdk_kms.types.marker_type


class ListAliasesResponse(TypedDict):
    aliases: NotRequired["aws_sdk_kms.types.alias_list.AliasList"]
    """<p>A list of aliases.</p>"""
    next_marker: NotRequired["aws_sdk_kms.types.marker_type.MarkerType"]
    """<p>When <code>Truncated</code> is true, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent request.</p>"""
    truncated: "aws_sdk_kms.types.boolean_type.BooleanType"
    """<p>A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the <code>NextMarker</code> element in this response to the <code>Marker</code> parameter in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAliasesResponse) -> dict:
    out: dict = {}
    if "aliases" in value:
        import aws_sdk_kms.types.alias_list

        out["Aliases"] = aws_sdk_kms.types.alias_list.serialize_aws_json_1_1(
            value["aliases"]
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    out["Truncated"] = value.get("truncated", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAliasesResponse:
    out: ListAliasesResponse = {}  # type: ignore[typeddict-item]
    if "Aliases" in data:
        import aws_sdk_kms.types.alias_list

        out["aliases"] = aws_sdk_kms.types.alias_list.deserialize_aws_json_1_1(
            data["Aliases"]
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Truncated" in data:
        out["truncated"] = data["Truncated"]
    else:
        out["truncated"] = False
    return out
