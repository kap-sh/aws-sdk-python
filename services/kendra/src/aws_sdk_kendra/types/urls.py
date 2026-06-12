"""Generated from Smithy shape ``com.amazonaws.kendra#Urls``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.seed_url_configuration
    import aws_sdk_kendra.types.site_maps_configuration


class Urls(TypedDict):
    seed_url_configuration: NotRequired[
        "aws_sdk_kendra.types.seed_url_configuration.SeedUrlConfiguration"
    ]
    """<p>Configuration of the seed or starting point URLs of the websites you want to crawl.</p> <p>You can choose to crawl only the website host names, or the website host names with subdomains, or the website host names with subdomains and other domains that the web pages link to.</p> <p>You can list up to 100 seed URLs.</p>"""
    site_maps_configuration: NotRequired[
        "aws_sdk_kendra.types.site_maps_configuration.SiteMapsConfiguration"
    ]
    """<p>Configuration of the sitemap URLs of the websites you want to crawl.</p> <p>Only URLs belonging to the same website host names are crawled. You can list up to three sitemap URLs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Urls) -> dict:
    out: dict = {}
    if "seed_url_configuration" in value:
        import aws_sdk_kendra.types.seed_url_configuration

        out["SeedUrlConfiguration"] = (
            aws_sdk_kendra.types.seed_url_configuration.serialize_aws_json_1_1(
                value["seed_url_configuration"]
            )
        )
    if "site_maps_configuration" in value:
        import aws_sdk_kendra.types.site_maps_configuration

        out["SiteMapsConfiguration"] = (
            aws_sdk_kendra.types.site_maps_configuration.serialize_aws_json_1_1(
                value["site_maps_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Urls:
    out: Urls = {}  # type: ignore[typeddict-item]
    if "SeedUrlConfiguration" in data:
        import aws_sdk_kendra.types.seed_url_configuration

        out["seed_url_configuration"] = (
            aws_sdk_kendra.types.seed_url_configuration.deserialize_aws_json_1_1(
                data["SeedUrlConfiguration"]
            )
        )
    if "SiteMapsConfiguration" in data:
        import aws_sdk_kendra.types.site_maps_configuration

        out["site_maps_configuration"] = (
            aws_sdk_kendra.types.site_maps_configuration.deserialize_aws_json_1_1(
                data["SiteMapsConfiguration"]
            )
        )
    return out
