"""Generated from Smithy shape ``com.amazonaws.kms#ListAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.alias_list
    import capo_kms.types.boolean_type
    import capo_kms.types.marker_type


class ListAliasesResponse(TypedDict, closed=True):
    aliases: NotRequired["capo_kms.types.alias_list.AliasList"]
    """<p>A list of aliases.</p>"""
    next_marker: NotRequired["capo_kms.types.marker_type.MarkerType"]
    """<p>When <code>Truncated</code> is true, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent request.</p>"""
    truncated: "capo_kms.types.boolean_type.BooleanType"
    """<p>A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the <code>NextMarker</code> element in this response to the <code>Marker</code> parameter in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAliasesResponse) -> dict:
    out: dict = {}
    if "aliases" in value:
        import capo_kms.types.alias_list

        out["Aliases"] = capo_kms.types.alias_list.serialize_aws_json_1_1(
            value["aliases"]
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    out["Truncated"] = value.get("truncated", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAliasesResponse:
    out: ListAliasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Aliases") is not None:
        import capo_kms.types.alias_list

        out["aliases"] = capo_kms.types.alias_list.deserialize_aws_json_1_1(
            data["Aliases"]
        )
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("Truncated") is not None:
        out["truncated"] = data["Truncated"]
    else:
        out["truncated"] = False
    return out
