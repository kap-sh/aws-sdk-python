"""Generated from Smithy shape ``com.amazonaws.organizations#UpdateResponsibilityTransferResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.responsibility_transfer


class UpdateResponsibilityTransferResponse(TypedDict):
    responsibility_transfer: NotRequired[
        "aws_sdk_organizations.types.responsibility_transfer.ResponsibilityTransfer"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResponsibilityTransferResponse) -> dict:
    out: dict = {}
    if "responsibility_transfer" in value:
        import aws_sdk_organizations.types.responsibility_transfer

        out["ResponsibilityTransfer"] = (
            aws_sdk_organizations.types.responsibility_transfer.serialize_aws_json_1_1(
                value["responsibility_transfer"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResponsibilityTransferResponse:
    out: UpdateResponsibilityTransferResponse = {}  # type: ignore[typeddict-item]
    if "ResponsibilityTransfer" in data:
        import aws_sdk_organizations.types.responsibility_transfer

        out["responsibility_transfer"] = (
            aws_sdk_organizations.types.responsibility_transfer.deserialize_aws_json_1_1(
                data["ResponsibilityTransfer"]
            )
        )
    return out
