"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateAwsLogSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.account_list


class CreateAwsLogSourceResponse(TypedDict):
    failed: NotRequired["aws_sdk_securitylake.types.account_list.AccountList"]
    """<p>Lists all accounts in which enabling a natively supported Amazon Web Services service as a Security Lake source failed. The failure occurred as these accounts are not part of an organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAwsLogSourceResponse) -> dict:
    out: dict = {}
    if "failed" in value:
        import aws_sdk_securitylake.types.account_list

        out["failed"] = aws_sdk_securitylake.types.account_list.serialize_json(
            value["failed"]
        )
    return out


def deserialize_json(data: dict) -> CreateAwsLogSourceResponse:
    out: CreateAwsLogSourceResponse = {}  # type: ignore[typeddict-item]
    if "failed" in data:
        import aws_sdk_securitylake.types.account_list

        out["failed"] = aws_sdk_securitylake.types.account_list.deserialize_json(
            data["failed"]
        )
    return out
