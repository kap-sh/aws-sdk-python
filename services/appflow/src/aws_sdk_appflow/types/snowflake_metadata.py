"""Generated from Smithy shape ``com.amazonaws.appflow#SnowflakeMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.region_list


class SnowflakeMetadata(TypedDict):
    supported_regions: NotRequired["aws_sdk_appflow.types.region_list.RegionList"]
    """<p> Specifies the supported Amazon Web Services Regions when using Snowflake. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeMetadata) -> dict:
    out: dict = {}
    if "supported_regions" in value:
        import aws_sdk_appflow.types.region_list

        out["supportedRegions"] = aws_sdk_appflow.types.region_list.serialize_json(
            value["supported_regions"]
        )
    return out


def deserialize_json(data: dict) -> SnowflakeMetadata:
    out: SnowflakeMetadata = {}  # type: ignore[typeddict-item]
    if "supportedRegions" in data:
        import aws_sdk_appflow.types.region_list

        out["supported_regions"] = aws_sdk_appflow.types.region_list.deserialize_json(
            data["supportedRegions"]
        )
    return out
