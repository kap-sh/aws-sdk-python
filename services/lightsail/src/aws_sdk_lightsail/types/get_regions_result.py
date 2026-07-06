"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRegionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.region_list


class GetRegionsResult(TypedDict, closed=True):
    regions: NotRequired["aws_sdk_lightsail.types.region_list.RegionList"]
    """<p>An array of key-value pairs containing information about your get regions request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRegionsResult) -> dict:
    out: dict = {}
    if "regions" in value:
        import aws_sdk_lightsail.types.region_list

        out["regions"] = aws_sdk_lightsail.types.region_list.serialize_aws_json_1_1(
            value["regions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRegionsResult:
    out: GetRegionsResult = {}  # type: ignore[typeddict-item]
    if "regions" in data:
        import aws_sdk_lightsail.types.region_list

        out["regions"] = aws_sdk_lightsail.types.region_list.deserialize_aws_json_1_1(
            data["regions"]
        )
    return out
