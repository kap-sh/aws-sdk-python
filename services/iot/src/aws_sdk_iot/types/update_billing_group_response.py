"""Generated from Smithy shape ``com.amazonaws.iot#UpdateBillingGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.version


class UpdateBillingGroupResponse(TypedDict, closed=True):
    version: "aws_sdk_iot.types.version.Version"
    """<p>The latest version of the billing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBillingGroupResponse) -> dict:
    out: dict = {}
    out["version"] = value.get("version", 0)
    return out


def deserialize_json(data: dict) -> UpdateBillingGroupResponse:
    out: UpdateBillingGroupResponse = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    return out
