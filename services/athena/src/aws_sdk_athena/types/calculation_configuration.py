"""Generated from Smithy shape ``com.amazonaws.athena#CalculationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.code_block


class CalculationConfiguration(TypedDict):
    code_block: NotRequired["aws_sdk_athena.types.code_block.CodeBlock"]
    """<p>A string that contains the code for the calculation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalculationConfiguration) -> dict:
    out: dict = {}
    if "code_block" in value:
        out["CodeBlock"] = value["code_block"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CalculationConfiguration:
    out: CalculationConfiguration = {}  # type: ignore[typeddict-item]
    if "CodeBlock" in data:
        out["code_block"] = data["CodeBlock"]
    return out
