"""Generated from Smithy shape ``com.amazonaws.athena#CalculationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.code_block


class CalculationConfiguration(TypedDict, closed=True):
    code_block: NotRequired["capo_athena.types.code_block.CodeBlock"]
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
