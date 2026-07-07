"""Generated from Smithy shape ``com.amazonaws.qapps#GetQAppInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qapps.types.app_version
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.uuid


class GetQAppInput(TypedDict, closed=True):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App to retrieve.</p>"""
    app_version: NotRequired["aws_sdk_qapps.types.app_version.AppVersion"]
    """<p>The version of the Q App.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQAppInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQAppInput:
    out: GetQAppInput = {}  # type: ignore[typeddict-item]
    return out
