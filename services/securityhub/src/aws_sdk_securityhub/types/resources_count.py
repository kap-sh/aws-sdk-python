"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesCount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.trends_value_count


class ResourcesCount(TypedDict, closed=True):
    all_resources: NotRequired[
        "aws_sdk_securityhub.types.trends_value_count.TrendsValueCount"
    ]
    """<p>The total count of all resources for the given time interval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesCount) -> dict:
    out: dict = {}
    if "all_resources" in value:
        out["AllResources"] = value["all_resources"]
    return out


def deserialize_json(data: dict) -> ResourcesCount:
    out: ResourcesCount = {}  # type: ignore[typeddict-item]
    if "AllResources" in data:
        out["all_resources"] = data["AllResources"]
    return out
