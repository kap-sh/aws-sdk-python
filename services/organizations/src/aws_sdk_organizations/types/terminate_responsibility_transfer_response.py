"""Generated from Smithy shape ``com.amazonaws.organizations#TerminateResponsibilityTransferResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.responsibility_transfer


class TerminateResponsibilityTransferResponse(TypedDict, closed=True):
    responsibility_transfer: NotRequired[
        "aws_sdk_organizations.types.responsibility_transfer.ResponsibilityTransfer"
    ]
    """<p>A <code>ResponsibilityTransfer</code> object. Contains details for a transfer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateResponsibilityTransferResponse) -> dict:
    out: dict = {}
    if "responsibility_transfer" in value:
        import aws_sdk_organizations.types.responsibility_transfer

        out["ResponsibilityTransfer"] = (
            aws_sdk_organizations.types.responsibility_transfer.serialize_aws_json_1_1(
                value["responsibility_transfer"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateResponsibilityTransferResponse:
    out: TerminateResponsibilityTransferResponse = {}  # type: ignore[typeddict-item]
    if "ResponsibilityTransfer" in data:
        import aws_sdk_organizations.types.responsibility_transfer

        out["responsibility_transfer"] = (
            aws_sdk_organizations.types.responsibility_transfer.deserialize_aws_json_1_1(
                data["ResponsibilityTransfer"]
            )
        )
    return out
