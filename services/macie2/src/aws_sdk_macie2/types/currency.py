"""Generated from Smithy shape ``com.amazonaws.macie2#Currency``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of currency that the data for an Amazon Macie usage metric is reported in. Possible values are:</p>"""
Currency: TypeAlias = Literal["USD",]


# --- restJson1 ser/de ---
def serialize_json(value: Currency) -> str:
    return value


def deserialize_json(data: str) -> Currency:
    return cast(Currency, data)
