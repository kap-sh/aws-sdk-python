"""Generated from Smithy shape ``com.amazonaws.qapps#GetQAppInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.app_version
    import capo_qapps.types.instance_id
    import capo_qapps.types.uuid


class GetQAppInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App to retrieve.</p>"""
    app_version: NotRequired["capo_qapps.types.app_version.AppVersion"]
    """<p>The version of the Q App.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQAppInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQAppInput:
    out: GetQAppInput = {}  # type: ignore[typeddict-item]
    return out
