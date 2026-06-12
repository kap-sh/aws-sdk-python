"""Generated from Smithy shape ``com.amazonaws.securitylake#CustomLogSourceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_securitylake.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_securitylake.types.aws_identity
    import aws_sdk_securitylake.types.custom_log_source_crawler_configuration

class CustomLogSourceConfiguration(TypedDict):
    crawler_configuration: "aws_sdk_securitylake.types.custom_log_source_crawler_configuration.CustomLogSourceCrawlerConfiguration"
    """<p>The configuration used for the Glue Crawler for a third-party custom source.</p>"""
    provider_identity: "aws_sdk_securitylake.types.aws_identity.AwsIdentity"
    """<p>The identity of the log provider for the third-party custom source.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CustomLogSourceConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_securitylake.types.custom_log_source_crawler_configuration
    out["crawlerConfiguration"] = aws_sdk_securitylake.types.custom_log_source_crawler_configuration.serialize_json(value["crawler_configuration"])
    import aws_sdk_securitylake.types.aws_identity
    out["providerIdentity"] = aws_sdk_securitylake.types.aws_identity.serialize_json(value["provider_identity"])
    return out


def deserialize_json(data: dict) -> CustomLogSourceConfiguration:
    out: CustomLogSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "crawlerConfiguration" in data:
        import aws_sdk_securitylake.types.custom_log_source_crawler_configuration
        out["crawler_configuration"] = aws_sdk_securitylake.types.custom_log_source_crawler_configuration.deserialize_json(data["crawlerConfiguration"])
    else:
        raise DeserializationError("CustomLogSourceConfiguration.crawler_configuration required")
    if "providerIdentity" in data:
        import aws_sdk_securitylake.types.aws_identity
        out["provider_identity"] = aws_sdk_securitylake.types.aws_identity.deserialize_json(data["providerIdentity"])
    else:
        raise DeserializationError("CustomLogSourceConfiguration.provider_identity required")
    return out