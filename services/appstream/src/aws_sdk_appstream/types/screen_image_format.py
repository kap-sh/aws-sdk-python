"""Generated from Smithy shape ``com.amazonaws.appstream#ScreenImageFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

"""<p>The image format for agent screen captures.</p> <ul> <li> <p>PNG - PNG format.</p> </li> <li> <p>JPEG - JPEG format.</p> </li> </ul>"""
ScreenImageFormat: TypeAlias = Literal[
    "PNG",
    "JPEG",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PNG",
        "JPEG",
    )
)


def serialize_aws_json_1_1(value: ScreenImageFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScreenImageFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScreenImageFormat value: {data!r}")
    return cast(ScreenImageFormat, data)
