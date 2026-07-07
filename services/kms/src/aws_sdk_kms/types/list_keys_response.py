"""Generated from Smithy shape ``com.amazonaws.kms#ListKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kms.types.boolean_type
    import aws_sdk_kms.types.key_list
    import aws_sdk_kms.types.marker_type


class ListKeysResponse(TypedDict, closed=True):
    keys: NotRequired["aws_sdk_kms.types.key_list.KeyList"]
    """<p>A list of KMS keys.</p>"""
    next_marker: NotRequired["aws_sdk_kms.types.marker_type.MarkerType"]
    """<p>When <code>Truncated</code> is true, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent request.</p>"""
    truncated: "aws_sdk_kms.types.boolean_type.BooleanType"
    """<p>A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the <code>NextMarker</code> element in this response to the <code>Marker</code> parameter in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListKeysResponse) -> dict:
    out: dict = {}
    if "keys" in value:
        import aws_sdk_kms.types.key_list

        out["Keys"] = aws_sdk_kms.types.key_list.serialize_aws_json_1_1(value["keys"])
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    out["Truncated"] = value.get("truncated", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListKeysResponse:
    out: ListKeysResponse = {}  # type: ignore[typeddict-item]
    if "Keys" in data:
        import aws_sdk_kms.types.key_list

        out["keys"] = aws_sdk_kms.types.key_list.deserialize_aws_json_1_1(data["Keys"])
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Truncated" in data:
        out["truncated"] = data["Truncated"]
    else:
        out["truncated"] = False
    return out
