"""Generated from Smithy shape ``com.amazonaws.workspacesweb#WallpaperImageInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.s3_uri
    import aws_sdk_workspaces_web.types.wallpaper_image


class _WallpaperImageInput_blob(TypedDict):
    blob: "aws_sdk_workspaces_web.types.wallpaper_image.WallpaperImage"


class _WallpaperImageInput_s3Uri(TypedDict):
    s3Uri: "aws_sdk_workspaces_web.types.s3_uri.S3Uri"


WallpaperImageInput: TypeAlias = _WallpaperImageInput_blob | _WallpaperImageInput_s3Uri


# --- restJson1 ser/de ---
def serialize_json(value: WallpaperImageInput) -> dict:
    if "blob" in value:
        import aws_sdk_workspaces_web.types.wallpaper_image

        return {
            "blob": aws_sdk_workspaces_web.types.wallpaper_image.serialize_json(
                value["blob"]
            )
        }
    elif "s3Uri" in value:
        return {"s3Uri": value["s3Uri"]}
    else:
        raise SerializationError("WallpaperImageInput: no variant present")


def deserialize_json(data: dict) -> WallpaperImageInput:
    if "blob" in data:
        import aws_sdk_workspaces_web.types.wallpaper_image

        return {
            "blob": aws_sdk_workspaces_web.types.wallpaper_image.deserialize_json(
                data["blob"]
            )
        }
    elif "s3Uri" in data:
        return {"s3Uri": data["s3Uri"]}
    else:
        raise DeserializationError("WallpaperImageInput: no recognized variant key")
