"""Generated from Smithy shape ``com.amazonaws.securityhub#NumberFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.double


class NumberFilter(TypedDict, closed=True):
    gte: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p>The greater-than-equal condition to be applied to a single field when querying for findings. </p>"""
    lte: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p>The less-than-equal condition to be applied to a single field when querying for findings. </p>"""
    eq: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p>The equal-to condition to be applied to a single field when querying for findings.</p>"""
    gt: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p> The greater-than condition to be applied to a single field when querying for findings. </p>"""
    lt: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p> The less-than condition to be applied to a single field when querying for findings. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumberFilter) -> dict:
    out: dict = {}
    if "gte" in value:
        out["Gte"] = value["gte"]
    if "lte" in value:
        out["Lte"] = value["lte"]
    if "eq" in value:
        out["Eq"] = value["eq"]
    if "gt" in value:
        out["Gt"] = value["gt"]
    if "lt" in value:
        out["Lt"] = value["lt"]
    return out


def deserialize_json(data: dict) -> NumberFilter:
    out: NumberFilter = {}  # type: ignore[typeddict-item]
    if "Gte" in data:
        out["gte"] = data["Gte"]
    if "Lte" in data:
        out["lte"] = data["Lte"]
    if "Eq" in data:
        out["eq"] = data["Eq"]
    if "Gt" in data:
        out["gt"] = data["Gt"]
    if "Lt" in data:
        out["lt"] = data["Lt"]
    return out
