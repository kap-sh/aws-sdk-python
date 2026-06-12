"""Generated from Smithy shape ``com.amazonaws.macie2#Currency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The type of currency that the data for an Amazon Macie usage metric is reported in. Possible values are:</p>"""
Currency: TypeAlias = Literal["USD",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("USD",))


def serialize_json(value: Currency) -> str:
    return value


def deserialize_json(data: str) -> Currency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Currency value: {data!r}")
    return cast(Currency, data)
