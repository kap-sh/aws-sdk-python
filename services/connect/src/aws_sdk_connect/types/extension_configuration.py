"""Generated from Smithy shape ``com.amazonaws.connect#ExtensionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.allowed_extensions_list


class ExtensionConfiguration(TypedDict):
    allowed_extensions: (
        "aws_sdk_connect.types.allowed_extensions_list.AllowedExtensionsList"
    )
    """<p>The list of allowed file extensions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtensionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.allowed_extensions_list

    out["AllowedExtensions"] = (
        aws_sdk_connect.types.allowed_extensions_list.serialize_json(
            value["allowed_extensions"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExtensionConfiguration:
    out: ExtensionConfiguration = {}  # type: ignore[typeddict-item]
    if "AllowedExtensions" in data:
        import aws_sdk_connect.types.allowed_extensions_list

        out["allowed_extensions"] = (
            aws_sdk_connect.types.allowed_extensions_list.deserialize_json(
                data["AllowedExtensions"]
            )
        )
    else:
        raise DeserializationError("ExtensionConfiguration.allowed_extensions required")
    return out
