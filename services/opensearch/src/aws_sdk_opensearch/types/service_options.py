"""Generated from Smithy shape ``com.amazonaws.opensearch#ServiceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.regions_list


class ServiceOptions(TypedDict, closed=True):
    supported_regions: NotRequired["aws_sdk_opensearch.types.regions_list.RegionsList"]
    """<p>The list of supported Regions for the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceOptions) -> dict:
    out: dict = {}
    if "supported_regions" in value:
        import aws_sdk_opensearch.types.regions_list

        out["SupportedRegions"] = aws_sdk_opensearch.types.regions_list.serialize_json(
            value["supported_regions"]
        )
    return out


def deserialize_json(data: dict) -> ServiceOptions:
    out: ServiceOptions = {}  # type: ignore[typeddict-item]
    if "SupportedRegions" in data:
        import aws_sdk_opensearch.types.regions_list

        out["supported_regions"] = (
            aws_sdk_opensearch.types.regions_list.deserialize_json(
                data["SupportedRegions"]
            )
        )
    return out
