"""Generated from Smithy shape ``com.amazonaws.medialive#HlsCdnSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.hls_akamai_settings
    import aws_sdk_medialive.types.hls_basic_put_settings
    import aws_sdk_medialive.types.hls_media_store_settings
    import aws_sdk_medialive.types.hls_s3_settings
    import aws_sdk_medialive.types.hls_webdav_settings


class HlsCdnSettings(TypedDict):
    hls_akamai_settings: NotRequired[
        "aws_sdk_medialive.types.hls_akamai_settings.HlsAkamaiSettings"
    ]
    hls_basic_put_settings: NotRequired[
        "aws_sdk_medialive.types.hls_basic_put_settings.HlsBasicPutSettings"
    ]
    hls_media_store_settings: NotRequired[
        "aws_sdk_medialive.types.hls_media_store_settings.HlsMediaStoreSettings"
    ]
    hls_s3_settings: NotRequired[
        "aws_sdk_medialive.types.hls_s3_settings.HlsS3Settings"
    ]
    hls_webdav_settings: NotRequired[
        "aws_sdk_medialive.types.hls_webdav_settings.HlsWebdavSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: HlsCdnSettings) -> dict:
    out: dict = {}
    if "hls_akamai_settings" in value:
        import aws_sdk_medialive.types.hls_akamai_settings

        out["hlsAkamaiSettings"] = (
            aws_sdk_medialive.types.hls_akamai_settings.serialize_json(
                value["hls_akamai_settings"]
            )
        )
    if "hls_basic_put_settings" in value:
        import aws_sdk_medialive.types.hls_basic_put_settings

        out["hlsBasicPutSettings"] = (
            aws_sdk_medialive.types.hls_basic_put_settings.serialize_json(
                value["hls_basic_put_settings"]
            )
        )
    if "hls_media_store_settings" in value:
        import aws_sdk_medialive.types.hls_media_store_settings

        out["hlsMediaStoreSettings"] = (
            aws_sdk_medialive.types.hls_media_store_settings.serialize_json(
                value["hls_media_store_settings"]
            )
        )
    if "hls_s3_settings" in value:
        import aws_sdk_medialive.types.hls_s3_settings

        out["hlsS3Settings"] = aws_sdk_medialive.types.hls_s3_settings.serialize_json(
            value["hls_s3_settings"]
        )
    if "hls_webdav_settings" in value:
        import aws_sdk_medialive.types.hls_webdav_settings

        out["hlsWebdavSettings"] = (
            aws_sdk_medialive.types.hls_webdav_settings.serialize_json(
                value["hls_webdav_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> HlsCdnSettings:
    out: HlsCdnSettings = {}  # type: ignore[typeddict-item]
    if "hlsAkamaiSettings" in data:
        import aws_sdk_medialive.types.hls_akamai_settings

        out["hls_akamai_settings"] = (
            aws_sdk_medialive.types.hls_akamai_settings.deserialize_json(
                data["hlsAkamaiSettings"]
            )
        )
    if "hlsBasicPutSettings" in data:
        import aws_sdk_medialive.types.hls_basic_put_settings

        out["hls_basic_put_settings"] = (
            aws_sdk_medialive.types.hls_basic_put_settings.deserialize_json(
                data["hlsBasicPutSettings"]
            )
        )
    if "hlsMediaStoreSettings" in data:
        import aws_sdk_medialive.types.hls_media_store_settings

        out["hls_media_store_settings"] = (
            aws_sdk_medialive.types.hls_media_store_settings.deserialize_json(
                data["hlsMediaStoreSettings"]
            )
        )
    if "hlsS3Settings" in data:
        import aws_sdk_medialive.types.hls_s3_settings

        out["hls_s3_settings"] = (
            aws_sdk_medialive.types.hls_s3_settings.deserialize_json(
                data["hlsS3Settings"]
            )
        )
    if "hlsWebdavSettings" in data:
        import aws_sdk_medialive.types.hls_webdav_settings

        out["hls_webdav_settings"] = (
            aws_sdk_medialive.types.hls_webdav_settings.deserialize_json(
                data["hlsWebdavSettings"]
            )
        )
    return out
