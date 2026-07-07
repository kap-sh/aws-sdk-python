"""Generated from Smithy shape ``com.amazonaws.guardduty#ItemDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.additional_info
    import aws_sdk_guardduty.types.non_empty_string
    import aws_sdk_guardduty.types.string


class ItemDetails(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>Amazon Resource Name (ARN) of the resource where the threat was detected.</p>"""
    item_path: NotRequired["aws_sdk_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>The path where the threat was detected.</p>"""
    hash: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The hash value of the infected item.</p>"""
    additional_info: NotRequired[
        "aws_sdk_guardduty.types.additional_info.AdditionalInfo"
    ]
    """<p>Additional information about the detected threat item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ItemDetails) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "item_path" in value:
        out["itemPath"] = value["item_path"]
    if "hash" in value:
        out["hash"] = value["hash"]
    if "additional_info" in value:
        import aws_sdk_guardduty.types.additional_info

        out["additionalInfo"] = aws_sdk_guardduty.types.additional_info.serialize_json(
            value["additional_info"]
        )
    return out


def deserialize_json(data: dict) -> ItemDetails:
    out: ItemDetails = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "itemPath" in data:
        out["item_path"] = data["itemPath"]
    if "hash" in data:
        out["hash"] = data["hash"]
    if "additionalInfo" in data:
        import aws_sdk_guardduty.types.additional_info

        out["additional_info"] = (
            aws_sdk_guardduty.types.additional_info.deserialize_json(
                data["additionalInfo"]
            )
        )
    return out
