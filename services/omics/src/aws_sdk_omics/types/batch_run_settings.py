"""Generated from Smithy shape ``com.amazonaws.omics#BatchRunSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_omics.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.inline_settings
    import aws_sdk_omics.types.s3_uri_settings


class _BatchRunSettings_inlineSettings(TypedDict, closed=True):
    inlineSettings: "aws_sdk_omics.types.inline_settings.InlineSettings"


class _BatchRunSettings_s3UriSettings(TypedDict, closed=True):
    s3UriSettings: "aws_sdk_omics.types.s3_uri_settings.S3UriSettings"


BatchRunSettings: TypeAlias = (
    _BatchRunSettings_inlineSettings | _BatchRunSettings_s3UriSettings
)


# --- restJson1 ser/de ---
def serialize_json(value: BatchRunSettings) -> dict:
    if "inlineSettings" in value:
        import aws_sdk_omics.types.inline_settings

        return {
            "inlineSettings": aws_sdk_omics.types.inline_settings.serialize_json(
                value["inlineSettings"]
            )
        }
    elif "s3UriSettings" in value:
        return {"s3UriSettings": value["s3UriSettings"]}
    else:
        raise SerializationError("BatchRunSettings: no variant present")


def deserialize_json(data: dict) -> BatchRunSettings:
    if "inlineSettings" in data:
        import aws_sdk_omics.types.inline_settings

        return {
            "inlineSettings": aws_sdk_omics.types.inline_settings.deserialize_json(
                data["inlineSettings"]
            )
        }
    elif "s3UriSettings" in data:
        return {"s3UriSettings": data["s3UriSettings"]}
    else:
        raise DeserializationError("BatchRunSettings: no recognized variant key")
