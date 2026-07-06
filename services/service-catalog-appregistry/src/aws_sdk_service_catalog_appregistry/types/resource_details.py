"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.tag_value


class ResourceDetails(TypedDict, closed=True):
    tag_value: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.tag_value.TagValue"
    ]
    """<p>The value of the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDetails) -> dict:
    out: dict = {}
    if "tag_value" in value:
        out["tagValue"] = value["tag_value"]
    return out


def deserialize_json(data: dict) -> ResourceDetails:
    out: ResourceDetails = {}  # type: ignore[typeddict-item]
    if "tagValue" in data:
        out["tag_value"] = data["tagValue"]
    return out
