"""Generated from Smithy shape ``com.amazonaws.iot#DescribeMitigationActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.mitigation_action_name


class DescribeMitigationActionRequest(TypedDict, closed=True):
    action_name: "aws_sdk_iot.types.mitigation_action_name.MitigationActionName"
    """<p>The friendly name that uniquely identifies the mitigation action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMitigationActionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeMitigationActionRequest:
    out: DescribeMitigationActionRequest = {}  # type: ignore[typeddict-item]
    return out
