"""Generated from Smithy shape ``com.amazonaws.kms#ListKeyRotationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.boolean_type
    import aws_sdk_kms.types.marker_type
    import aws_sdk_kms.types.rotations_list


class ListKeyRotationsResponse(TypedDict):
    rotations: NotRequired["aws_sdk_kms.types.rotations_list.RotationsList"]
    """<p>A list of completed key material rotations. When the optional input parameter <code>IncludeKeyMaterial</code> is specified with a value of <code>ALL_KEY_MATERIAL</code>, this list includes the first key material and any imported key material pending rotation.</p>"""
    next_marker: NotRequired["aws_sdk_kms.types.marker_type.MarkerType"]
    """<p>When <code>Truncated</code> is true, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent request.</p>"""
    truncated: "aws_sdk_kms.types.boolean_type.BooleanType"
    """<p>A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the <code>NextMarker</code> element in this response to the <code>Marker</code> parameter in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListKeyRotationsResponse) -> dict:
    out: dict = {}
    if "rotations" in value:
        import aws_sdk_kms.types.rotations_list

        out["Rotations"] = aws_sdk_kms.types.rotations_list.serialize_aws_json_1_1(
            value["rotations"]
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    out["Truncated"] = value.get("truncated", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListKeyRotationsResponse:
    out: ListKeyRotationsResponse = {}  # type: ignore[typeddict-item]
    if "Rotations" in data:
        import aws_sdk_kms.types.rotations_list

        out["rotations"] = aws_sdk_kms.types.rotations_list.deserialize_aws_json_1_1(
            data["Rotations"]
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Truncated" in data:
        out["truncated"] = data["Truncated"]
    else:
        out["truncated"] = False
    return out
