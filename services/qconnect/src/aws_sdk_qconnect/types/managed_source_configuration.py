"""Generated from Smithy shape ``com.amazonaws.qconnect#ManagedSourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.web_crawler_configuration


class _ManagedSourceConfiguration_webCrawlerConfiguration(TypedDict, closed=True):
    webCrawlerConfiguration: (
        "aws_sdk_qconnect.types.web_crawler_configuration.WebCrawlerConfiguration"
    )


ManagedSourceConfiguration: TypeAlias = (
    _ManagedSourceConfiguration_webCrawlerConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: ManagedSourceConfiguration) -> dict:
    if "webCrawlerConfiguration" in value:
        import aws_sdk_qconnect.types.web_crawler_configuration

        return {
            "webCrawlerConfiguration": aws_sdk_qconnect.types.web_crawler_configuration.serialize_json(
                value["webCrawlerConfiguration"]
            )
        }
    else:
        raise SerializationError("ManagedSourceConfiguration: no variant present")


def deserialize_json(data: dict) -> ManagedSourceConfiguration:
    if "webCrawlerConfiguration" in data:
        import aws_sdk_qconnect.types.web_crawler_configuration

        return {
            "webCrawlerConfiguration": aws_sdk_qconnect.types.web_crawler_configuration.deserialize_json(
                data["webCrawlerConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "ManagedSourceConfiguration: no recognized variant key"
        )
