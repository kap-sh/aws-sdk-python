"""Generated from Smithy shape ``com.amazonaws.pinpoint#__TimezoneEstimationMethodsElement``."""

from typing import Literal, TypeAlias, cast

__TimezoneEstimationMethodsElement: TypeAlias = Literal[
    "PHONE_NUMBER",
    "POSTAL_CODE",
]


# --- restJson1 ser/de ---
def serialize_json(value: __TimezoneEstimationMethodsElement) -> str:
    return value


def deserialize_json(data: str) -> __TimezoneEstimationMethodsElement:
    return cast(__TimezoneEstimationMethodsElement, data)
