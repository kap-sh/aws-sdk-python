"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricDimensionName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The <code>BatchGetMetricDataQuery</code> dimension name. This can be one of the following:</p> <ul> <li> <p> <code>EMAIL_IDENTITY</code> – The email identity used when sending messages.</p> </li> <li> <p> <code>CONFIGURATION_SET</code> – The configuration set used when sending messages (if one was used).</p> </li> <li> <p> <code>ISP</code> – The recipient ISP (e.g. <code>Gmail</code>, <code>Yahoo</code>, etc.).</p> </li> </ul>"""
MetricDimensionName: TypeAlias = Literal[
    "EMAIL_IDENTITY",
    "CONFIGURATION_SET",
    "ISP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMAIL_IDENTITY",
        "CONFIGURATION_SET",
        "ISP",
    )
)


def serialize_json(value: MetricDimensionName) -> str:
    return value


def deserialize_json(data: str) -> MetricDimensionName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricDimensionName value: {data!r}")
    return cast(MetricDimensionName, data)
