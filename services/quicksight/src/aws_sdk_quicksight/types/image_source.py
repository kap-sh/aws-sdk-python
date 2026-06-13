"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageSource``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string


class _ImageSource_PublicUrl(TypedDict):
    PublicUrl: "aws_sdk_quicksight.types.string.String"


class _ImageSource_S3Uri(TypedDict):
    S3Uri: "aws_sdk_quicksight.types.string.String"


ImageSource: TypeAlias = _ImageSource_PublicUrl | _ImageSource_S3Uri


# --- restJson1 ser/de ---
def serialize_json(value: ImageSource) -> dict:
    if "PublicUrl" in value:
        return {"PublicUrl": value["PublicUrl"]}
    elif "S3Uri" in value:
        return {"S3Uri": value["S3Uri"]}
    else:
        raise SerializationError("ImageSource: no variant present")


def deserialize_json(data: dict) -> ImageSource:
    if "PublicUrl" in data:
        return {"PublicUrl": data["PublicUrl"]}
    elif "S3Uri" in data:
        return {"S3Uri": data["S3Uri"]}
    else:
        raise DeserializationError("ImageSource: no recognized variant key")
