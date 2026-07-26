"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionTypeBrief``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.capabilities
    import capo_glue.types.connection_type
    import capo_glue.types.connection_type_variant_list
    import capo_glue.types.description
    import capo_glue.types.display_name
    import capo_glue.types.list_of_string
    import capo_glue.types.url_string
    import capo_glue.types.vendor


class ConnectionTypeBrief(TypedDict, closed=True):
    connection_type: NotRequired["capo_glue.types.connection_type.ConnectionType"]
    """<p>The name of the connection type.</p>"""
    display_name: NotRequired["capo_glue.types.display_name.DisplayName"]
    """<p>The human-readable name for the connection type that is displayed in the Glue console.</p>"""
    vendor: NotRequired["capo_glue.types.vendor.Vendor"]
    """<p>The name of the vendor or provider that created or maintains this connection type.</p>"""
    description: NotRequired["capo_glue.types.description.Description"]
    """<p>A description of the connection type.</p>"""
    categories: NotRequired["capo_glue.types.list_of_string.ListOfString"]
    """<p>A list of categories that this connection type belongs to. Categories help users filter and find appropriate connection types based on their use cases.</p>"""
    capabilities: NotRequired["capo_glue.types.capabilities.Capabilities"]
    """<p>The supported authentication types, data interface types (compute environments), and data operations of the connector.</p>"""
    logo_url: NotRequired["capo_glue.types.url_string.UrlString"]
    """<p>The URL of the logo associated with a connection type.</p>"""
    connection_type_variants: NotRequired[
        "capo_glue.types.connection_type_variant_list.ConnectionTypeVariantList"
    ]
    """<p>A list of variants available for this connection type. Different variants may provide specialized configurations for specific use cases or implementations of the same general connection type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionTypeBrief) -> dict:
    out: dict = {}
    if "connection_type" in value:
        import capo_glue.types.connection_type

        out["ConnectionType"] = capo_glue.types.connection_type.serialize_aws_json_1_1(
            value["connection_type"]
        )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "vendor" in value:
        out["Vendor"] = value["vendor"]
    if "description" in value:
        out["Description"] = value["description"]
    if "categories" in value:
        import capo_glue.types.list_of_string

        out["Categories"] = capo_glue.types.list_of_string.serialize_aws_json_1_1(
            value["categories"]
        )
    if "capabilities" in value:
        import capo_glue.types.capabilities

        out["Capabilities"] = capo_glue.types.capabilities.serialize_aws_json_1_1(
            value["capabilities"]
        )
    if "logo_url" in value:
        out["LogoUrl"] = value["logo_url"]
    if "connection_type_variants" in value:
        import capo_glue.types.connection_type_variant_list

        out["ConnectionTypeVariants"] = (
            capo_glue.types.connection_type_variant_list.serialize_aws_json_1_1(
                value["connection_type_variants"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionTypeBrief:
    out: ConnectionTypeBrief = {}  # type: ignore[typeddict-item]
    if "ConnectionType" in data:
        import capo_glue.types.connection_type

        out["connection_type"] = (
            capo_glue.types.connection_type.deserialize_aws_json_1_1(
                data["ConnectionType"]
            )
        )
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Vendor" in data:
        out["vendor"] = data["Vendor"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Categories" in data:
        import capo_glue.types.list_of_string

        out["categories"] = capo_glue.types.list_of_string.deserialize_aws_json_1_1(
            data["Categories"]
        )
    if "Capabilities" in data:
        import capo_glue.types.capabilities

        out["capabilities"] = capo_glue.types.capabilities.deserialize_aws_json_1_1(
            data["Capabilities"]
        )
    if "LogoUrl" in data:
        out["logo_url"] = data["LogoUrl"]
    if "ConnectionTypeVariants" in data:
        import capo_glue.types.connection_type_variant_list

        out["connection_type_variants"] = (
            capo_glue.types.connection_type_variant_list.deserialize_aws_json_1_1(
                data["ConnectionTypeVariants"]
            )
        )
    return out
