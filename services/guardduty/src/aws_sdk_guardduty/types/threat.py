"""Generated from Smithy shape ``com.amazonaws.guardduty#Threat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.item_details_list
    import aws_sdk_guardduty.types.item_paths
    import aws_sdk_guardduty.types.long
    import aws_sdk_guardduty.types.string


class Threat(TypedDict, closed=True):
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Name of the detected threat that caused GuardDuty to generate this finding.</p>"""
    source: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Source of the threat that generated this finding.</p>"""
    item_paths: NotRequired["aws_sdk_guardduty.types.item_paths.ItemPaths"]
    """<p>Information about the nested item path and hash of the protected resource.</p>"""
    count: NotRequired["aws_sdk_guardduty.types.long.Long"]
    """<p>The number of occurrences of this specific threat detected during the scan.</p>"""
    hash: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The hash identifier of the detected malware threat.</p>"""
    item_details: NotRequired[
        "aws_sdk_guardduty.types.item_details_list.ItemDetailsList"
    ]
    """<p>Detailed information about the detected malware threat.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Threat) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "source" in value:
        out["source"] = value["source"]
    if "item_paths" in value:
        import aws_sdk_guardduty.types.item_paths

        out["itemPaths"] = aws_sdk_guardduty.types.item_paths.serialize_json(
            value["item_paths"]
        )
    if "count" in value:
        out["count"] = value["count"]
    if "hash" in value:
        out["hash"] = value["hash"]
    if "item_details" in value:
        import aws_sdk_guardduty.types.item_details_list

        out["itemDetails"] = aws_sdk_guardduty.types.item_details_list.serialize_json(
            value["item_details"]
        )
    return out


def deserialize_json(data: dict) -> Threat:
    out: Threat = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "source" in data:
        out["source"] = data["source"]
    if "itemPaths" in data:
        import aws_sdk_guardduty.types.item_paths

        out["item_paths"] = aws_sdk_guardduty.types.item_paths.deserialize_json(
            data["itemPaths"]
        )
    if "count" in data:
        out["count"] = data["count"]
    if "hash" in data:
        out["hash"] = data["hash"]
    if "itemDetails" in data:
        import aws_sdk_guardduty.types.item_details_list

        out["item_details"] = (
            aws_sdk_guardduty.types.item_details_list.deserialize_json(
                data["itemDetails"]
            )
        )
    return out
