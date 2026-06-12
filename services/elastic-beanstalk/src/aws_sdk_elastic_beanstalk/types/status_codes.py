"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#StatusCodes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.nullable_integer


class StatusCodes(TypedDict):
    status2xx: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_integer.NullableInteger"
    ]
    """<p>The percentage of requests over the last 10 seconds that resulted in a 2xx (200, 201, etc.) status code.</p>"""
    status3xx: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_integer.NullableInteger"
    ]
    """<p>The percentage of requests over the last 10 seconds that resulted in a 3xx (300, 301, etc.) status code.</p>"""
    status4xx: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_integer.NullableInteger"
    ]
    """<p>The percentage of requests over the last 10 seconds that resulted in a 4xx (400, 401, etc.) status code.</p>"""
    status5xx: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_integer.NullableInteger"
    ]
    """<p>The percentage of requests over the last 10 seconds that resulted in a 5xx (500, 501, etc.) status code.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StatusCodes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status2xx" in value:
        pairs.append((f"{prefix}.Status2xx", str(value["status2xx"])))
    if "status3xx" in value:
        pairs.append((f"{prefix}.Status3xx", str(value["status3xx"])))
    if "status4xx" in value:
        pairs.append((f"{prefix}.Status4xx", str(value["status4xx"])))
    if "status5xx" in value:
        pairs.append((f"{prefix}.Status5xx", str(value["status5xx"])))


def deserialize_query(el: Element) -> StatusCodes:
    out: StatusCodes = {}  # type: ignore[typeddict-item]
    child_status2xx = el.find("Status2xx")
    if child_status2xx is not None:
        out["status2xx"] = int(child_status2xx.text or "")
    child_status3xx = el.find("Status3xx")
    if child_status3xx is not None:
        out["status3xx"] = int(child_status3xx.text or "")
    child_status4xx = el.find("Status4xx")
    if child_status4xx is not None:
        out["status4xx"] = int(child_status4xx.text or "")
    child_status5xx = el.find("Status5xx")
    if child_status5xx is not None:
        out["status5xx"] = int(child_status5xx.text or "")
    return out
