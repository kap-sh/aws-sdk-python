"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionTypeVariant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.description
    import capo_glue.types.display_name
    import capo_glue.types.url_string


class ConnectionTypeVariant(TypedDict, closed=True):
    connection_type_variant_name: NotRequired[
        "capo_glue.types.display_name.DisplayName"
    ]
    """<p>The unique identifier for the connection type variant. This name is used internally to identify the specific variant of a connection type. </p>"""
    display_name: NotRequired["capo_glue.types.display_name.DisplayName"]
    """<p>The human-readable name for the connection type variant that is displayed in the Glue console.</p>"""
    description: NotRequired["capo_glue.types.description.Description"]
    """<p>A detailed description of the connection type variant, including its purpose, use cases, and any specific configuration requirements.</p>"""
    logo_url: NotRequired["capo_glue.types.url_string.UrlString"]
    """<p>The URL of the logo associated with a connection type variant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionTypeVariant) -> dict:
    out: dict = {}
    if "connection_type_variant_name" in value:
        out["ConnectionTypeVariantName"] = value["connection_type_variant_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "logo_url" in value:
        out["LogoUrl"] = value["logo_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionTypeVariant:
    out: ConnectionTypeVariant = {}  # type: ignore[typeddict-item]
    if "ConnectionTypeVariantName" in data:
        out["connection_type_variant_name"] = data["ConnectionTypeVariantName"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LogoUrl" in data:
        out["logo_url"] = data["LogoUrl"]
    return out
