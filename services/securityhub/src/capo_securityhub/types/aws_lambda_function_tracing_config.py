"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaFunctionTracingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsLambdaFunctionTracingConfig(TypedDict, closed=True):
    mode: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The tracing mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaFunctionTracingConfig) -> dict:
    out: dict = {}
    if "mode" in value:
        out["Mode"] = value["mode"]
    return out


def deserialize_json(data: dict) -> AwsLambdaFunctionTracingConfig:
    out: AwsLambdaFunctionTracingConfig = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        out["mode"] = data["Mode"]
    return out
