"""Generated from Smithy shape ``com.amazonaws.guardduty#GetMasterAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.master


class GetMasterAccountResponse(TypedDict):
    master: NotRequired["aws_sdk_guardduty.types.master.Master"]
    """<p>The administrator account details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMasterAccountResponse) -> dict:
    out: dict = {}
    if "master" in value:
        import aws_sdk_guardduty.types.master

        out["master"] = aws_sdk_guardduty.types.master.serialize_json(value["master"])
    return out


def deserialize_json(data: dict) -> GetMasterAccountResponse:
    out: GetMasterAccountResponse = {}  # type: ignore[typeddict-item]
    if "master" in data:
        import aws_sdk_guardduty.types.master

        out["master"] = aws_sdk_guardduty.types.master.deserialize_json(data["master"])
    return out
