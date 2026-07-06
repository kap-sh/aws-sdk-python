"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateMemberSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.macie_status


class UpdateMemberSessionRequest(TypedDict, closed=True):
    id: "aws_sdk_macie2.types.__string.__string"
    """<p>The unique identifier for the Amazon Macie resource that the request applies to.</p>"""
    status: NotRequired["aws_sdk_macie2.types.macie_status.MacieStatus"]
    """<p>Specifies the new status for the account. Valid values are: ENABLED, resume all Amazon Macie activities for the account; and, PAUSED, suspend all Macie activities for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMemberSessionRequest) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_macie2.types.macie_status

        out["status"] = aws_sdk_macie2.types.macie_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateMemberSessionRequest:
    out: UpdateMemberSessionRequest = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_macie2.types.macie_status

        out["status"] = aws_sdk_macie2.types.macie_status.deserialize_json(
            data["status"]
        )
    return out
