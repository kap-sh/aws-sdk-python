"""Generated from Smithy shape ``com.amazonaws.appstream#ScreenResolution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

"""<p>The screen resolution for the agent streaming environment.</p> <ul> <li> <p>W_1280xH_720 - 1280 x 720 pixels.</p> </li> </ul>"""
ScreenResolution: TypeAlias = Literal["W_1280xH_720",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("W_1280xH_720",))


def serialize_aws_json_1_1(value: ScreenResolution) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScreenResolution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScreenResolution value: {data!r}")
    return cast(ScreenResolution, data)
