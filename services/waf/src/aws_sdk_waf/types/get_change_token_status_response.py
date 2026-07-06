"""Generated from Smithy shape ``com.amazonaws.waf#GetChangeTokenStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_token_status


class GetChangeTokenStatusResponse(TypedDict, closed=True):
    change_token_status: NotRequired[
        "aws_sdk_waf.types.change_token_status.ChangeTokenStatus"
    ]
    """<p>The status of the change token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetChangeTokenStatusResponse) -> dict:
    out: dict = {}
    if "change_token_status" in value:
        import aws_sdk_waf.types.change_token_status

        out["ChangeTokenStatus"] = (
            aws_sdk_waf.types.change_token_status.serialize_aws_json_1_1(
                value["change_token_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetChangeTokenStatusResponse:
    out: GetChangeTokenStatusResponse = {}  # type: ignore[typeddict-item]
    if "ChangeTokenStatus" in data:
        import aws_sdk_waf.types.change_token_status

        out["change_token_status"] = (
            aws_sdk_waf.types.change_token_status.deserialize_aws_json_1_1(
                data["ChangeTokenStatus"]
            )
        )
    return out
