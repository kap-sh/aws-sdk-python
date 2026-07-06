"""Generated from Smithy shape ``com.amazonaws.m2#PoAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.string20_list


class PoAttributes(TypedDict, closed=True):
    format: "str"
    """<p>The format of the data set records.</p>"""
    encoding: NotRequired["str"]
    """<p>The character set encoding of the data set.</p>"""
    member_file_extensions: "aws_sdk_m2.types.string20_list.String20List"
    """<p>An array containing one or more filename extensions, allowing you to specify which files to be included as PDS member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PoAttributes) -> dict:
    out: dict = {}
    out["format"] = value["format"]
    if "encoding" in value:
        out["encoding"] = value["encoding"]
    import aws_sdk_m2.types.string20_list

    out["memberFileExtensions"] = aws_sdk_m2.types.string20_list.serialize_json(
        value["member_file_extensions"]
    )
    return out


def deserialize_json(data: dict) -> PoAttributes:
    out: PoAttributes = {}  # type: ignore[typeddict-item]
    if "format" in data:
        out["format"] = data["format"]
    else:
        raise DeserializationError("PoAttributes.format required")
    if "encoding" in data:
        out["encoding"] = data["encoding"]
    if "memberFileExtensions" in data:
        import aws_sdk_m2.types.string20_list

        out["member_file_extensions"] = aws_sdk_m2.types.string20_list.deserialize_json(
            data["memberFileExtensions"]
        )
    else:
        raise DeserializationError("PoAttributes.member_file_extensions required")
    return out
