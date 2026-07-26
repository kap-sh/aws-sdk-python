"""Generated from Smithy shape ``com.amazonaws.athena#GetCalculationExecutionCodeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.code_block


class GetCalculationExecutionCodeResponse(TypedDict, closed=True):
    code_block: NotRequired["capo_athena.types.code_block.CodeBlock"]
    """<p>The unencrypted code that was executed for the calculation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCalculationExecutionCodeResponse) -> dict:
    out: dict = {}
    if "code_block" in value:
        out["CodeBlock"] = value["code_block"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCalculationExecutionCodeResponse:
    out: GetCalculationExecutionCodeResponse = {}  # type: ignore[typeddict-item]
    if "CodeBlock" in data:
        out["code_block"] = data["CodeBlock"]
    return out
