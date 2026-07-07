"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IconImageInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.icon_image
    import aws_sdk_workspaces_web.types.s3_uri


class _IconImageInput_blob(TypedDict, closed=True):
    blob: "aws_sdk_workspaces_web.types.icon_image.IconImage"


class _IconImageInput_s3Uri(TypedDict, closed=True):
    s3Uri: "aws_sdk_workspaces_web.types.s3_uri.S3Uri"


IconImageInput: TypeAlias = _IconImageInput_blob | _IconImageInput_s3Uri


# --- restJson1 ser/de ---
def serialize_json(value: IconImageInput) -> dict:
    if "blob" in value:
        import aws_sdk_workspaces_web.types.icon_image

        return {
            "blob": aws_sdk_workspaces_web.types.icon_image.serialize_json(
                value["blob"]
            )
        }
    elif "s3Uri" in value:
        return {"s3Uri": value["s3Uri"]}
    else:
        raise SerializationError("IconImageInput: no variant present")


def deserialize_json(data: dict) -> IconImageInput:
    if "blob" in data:
        import aws_sdk_workspaces_web.types.icon_image

        return {
            "blob": aws_sdk_workspaces_web.types.icon_image.deserialize_json(
                data["blob"]
            )
        }
    elif "s3Uri" in data:
        return {"s3Uri": data["s3Uri"]}
    else:
        raise DeserializationError("IconImageInput: no recognized variant key")
