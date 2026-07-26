"""Generated from Smithy shape ``com.amazonaws.securityhub#StatelessCustomPublishMetricActionDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class StatelessCustomPublishMetricActionDimension(TypedDict, closed=True):
    value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value to use for the custom metric dimension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatelessCustomPublishMetricActionDimension) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> StatelessCustomPublishMetricActionDimension:
    out: StatelessCustomPublishMetricActionDimension = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
