"""Generated from Smithy shape ``com.amazonaws.securitylake#CustomLogSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securitylake.types.aws_identity
    import capo_securitylake.types.custom_log_source_crawler_configuration


class CustomLogSourceConfiguration(TypedDict, closed=True):
    crawler_configuration: "capo_securitylake.types.custom_log_source_crawler_configuration.CustomLogSourceCrawlerConfiguration"
    """<p>The configuration used for the Glue Crawler for a third-party custom source.</p>"""
    provider_identity: "capo_securitylake.types.aws_identity.AwsIdentity"
    """<p>The identity of the log provider for the third-party custom source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLogSourceConfiguration) -> dict:
    out: dict = {}
    import capo_securitylake.types.custom_log_source_crawler_configuration

    out["crawlerConfiguration"] = (
        capo_securitylake.types.custom_log_source_crawler_configuration.serialize_json(
            value["crawler_configuration"]
        )
    )
    import capo_securitylake.types.aws_identity

    out["providerIdentity"] = capo_securitylake.types.aws_identity.serialize_json(
        value["provider_identity"]
    )
    return out


def deserialize_json(data: dict) -> CustomLogSourceConfiguration:
    out: CustomLogSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "crawlerConfiguration" in data:
        import capo_securitylake.types.custom_log_source_crawler_configuration

        out["crawler_configuration"] = (
            capo_securitylake.types.custom_log_source_crawler_configuration.deserialize_json(
                data["crawlerConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CustomLogSourceConfiguration.crawler_configuration required"
        )
    if "providerIdentity" in data:
        import capo_securitylake.types.aws_identity

        out["provider_identity"] = (
            capo_securitylake.types.aws_identity.deserialize_json(
                data["providerIdentity"]
            )
        )
    else:
        raise DeserializationError(
            "CustomLogSourceConfiguration.provider_identity required"
        )
    return out
