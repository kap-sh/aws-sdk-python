"""Generated from Smithy shape ``com.amazonaws.fis#ResolvedTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.target_information_map
    import aws_sdk_fis.types.target_name
    import aws_sdk_fis.types.target_resource_type_id


class ResolvedTarget(TypedDict, closed=True):
    resource_type: NotRequired[
        "aws_sdk_fis.types.target_resource_type_id.TargetResourceTypeId"
    ]
    """<p>The resource type of the target.</p>"""
    target_name: NotRequired["aws_sdk_fis.types.target_name.TargetName"]
    """<p>The name of the target.</p>"""
    target_information: NotRequired[
        "aws_sdk_fis.types.target_information_map.TargetInformationMap"
    ]
    """<p>Information about the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResolvedTarget) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "target_name" in value:
        out["targetName"] = value["target_name"]
    if "target_information" in value:
        import aws_sdk_fis.types.target_information_map

        out["targetInformation"] = (
            aws_sdk_fis.types.target_information_map.serialize_json(
                value["target_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResolvedTarget:
    out: ResolvedTarget = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "targetName" in data:
        out["target_name"] = data["targetName"]
    if "targetInformation" in data:
        import aws_sdk_fis.types.target_information_map

        out["target_information"] = (
            aws_sdk_fis.types.target_information_map.deserialize_json(
                data["targetInformation"]
            )
        )
    return out
