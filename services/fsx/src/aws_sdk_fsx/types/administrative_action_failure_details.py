"""Generated from Smithy shape ``com.amazonaws.fsx#AdministrativeActionFailureDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message


class AdministrativeActionFailureDetails(TypedDict):
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]
    """<p>Error message providing details about the failed administrative action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdministrativeActionFailureDetails) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdministrativeActionFailureDetails:
    out: AdministrativeActionFailureDetails = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
