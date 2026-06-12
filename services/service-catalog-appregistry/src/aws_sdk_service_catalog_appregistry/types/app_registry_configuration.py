"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AppRegistryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.tag_query_configuration


class AppRegistryConfiguration(TypedDict):
    tag_query_configuration: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.tag_query_configuration.TagQueryConfiguration"
    ]
    """<p> Includes the definition of a <code>tagQuery</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppRegistryConfiguration) -> dict:
    out: dict = {}
    if "tag_query_configuration" in value:
        import aws_sdk_service_catalog_appregistry.types.tag_query_configuration

        out["tagQueryConfiguration"] = (
            aws_sdk_service_catalog_appregistry.types.tag_query_configuration.serialize_json(
                value["tag_query_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AppRegistryConfiguration:
    out: AppRegistryConfiguration = {}  # type: ignore[typeddict-item]
    if "tagQueryConfiguration" in data:
        import aws_sdk_service_catalog_appregistry.types.tag_query_configuration

        out["tag_query_configuration"] = (
            aws_sdk_service_catalog_appregistry.types.tag_query_configuration.deserialize_json(
                data["tagQueryConfiguration"]
            )
        )
    return out
