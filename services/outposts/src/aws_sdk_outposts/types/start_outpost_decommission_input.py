"""Generated from Smithy shape ``com.amazonaws.outposts#StartOutpostDecommissionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.outpost_identifier
    import aws_sdk_outposts.types.validate_only


class StartOutpostDecommissionInput(TypedDict, closed=True):
    outpost_identifier: "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>The ID or ARN of the Outpost that you want to decommission.</p>"""
    validate_only: "aws_sdk_outposts.types.validate_only.ValidateOnly"
    """<p>Validates the request without starting the decommission process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOutpostDecommissionInput) -> dict:
    out: dict = {}
    out["ValidateOnly"] = value.get("validate_only", False)
    return out


def deserialize_json(data: dict) -> StartOutpostDecommissionInput:
    out: StartOutpostDecommissionInput = {}  # type: ignore[typeddict-item]
    if "ValidateOnly" in data:
        out["validate_only"] = data["ValidateOnly"]
    else:
        out["validate_only"] = False
    return out
