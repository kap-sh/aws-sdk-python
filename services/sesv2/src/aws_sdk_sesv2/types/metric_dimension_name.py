"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricDimensionName``."""

from typing import Literal, TypeAlias, cast

"""<p>The <code>BatchGetMetricDataQuery</code> dimension name. This can be one of the following:</p> <ul> <li> <p> <code>EMAIL_IDENTITY</code> – The email identity used when sending messages.</p> </li> <li> <p> <code>CONFIGURATION_SET</code> – The configuration set used when sending messages (if one was used).</p> </li> <li> <p> <code>ISP</code> – The recipient ISP (e.g. <code>Gmail</code>, <code>Yahoo</code>, etc.).</p> </li> </ul>"""
MetricDimensionName: TypeAlias = Literal[
    "EMAIL_IDENTITY",
    "CONFIGURATION_SET",
    "ISP",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricDimensionName) -> str:
    return value


def deserialize_json(data: str) -> MetricDimensionName:
    return cast(MetricDimensionName, data)
