"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#TagQueryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.tag_key_config


class TagQueryConfiguration(TypedDict, closed=True):
    tag_key: NotRequired[
        "capo_service_catalog_appregistry.types.tag_key_config.TagKeyConfig"
    ]
    """<p> Condition in the IAM policy that associates resources to an application. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagQueryConfiguration) -> dict:
    out: dict = {}
    if "tag_key" in value:
        out["tagKey"] = value["tag_key"]
    return out


def deserialize_json(data: dict) -> TagQueryConfiguration:
    out: TagQueryConfiguration = {}  # type: ignore[typeddict-item]
    if "tagKey" in data:
        out["tag_key"] = data["tagKey"]
    return out
