"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesTrendsValues``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resources_count


class ResourcesTrendsValues(TypedDict):
    resources_count: NotRequired[
        "aws_sdk_securityhub.types.resources_count.ResourcesCount"
    ]
    """<p>The resource count statistics for this data point in the trend timeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesTrendsValues) -> dict:
    out: dict = {}
    if "resources_count" in value:
        import aws_sdk_securityhub.types.resources_count

        out["ResourcesCount"] = (
            aws_sdk_securityhub.types.resources_count.serialize_json(
                value["resources_count"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourcesTrendsValues:
    out: ResourcesTrendsValues = {}  # type: ignore[typeddict-item]
    if "ResourcesCount" in data:
        import aws_sdk_securityhub.types.resources_count

        out["resources_count"] = (
            aws_sdk_securityhub.types.resources_count.deserialize_json(
                data["ResourcesCount"]
            )
        )
    return out
