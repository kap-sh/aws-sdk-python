"""Generated from Smithy shape ``com.amazonaws.guardduty#DomainDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class DomainDetails(TypedDict, closed=True):
    domain: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The domain information for the Amazon Web Services API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainDetails) -> dict:
    out: dict = {}
    if "domain" in value:
        out["domain"] = value["domain"]
    return out


def deserialize_json(data: dict) -> DomainDetails:
    out: DomainDetails = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    return out
