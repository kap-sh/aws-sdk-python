"""Generated from Smithy shape ``com.amazonaws.ssm#GetParameterResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameter


class GetParameterResult(TypedDict):
    parameter: NotRequired["aws_sdk_ssm.types.parameter.Parameter"]
    """<p>Information about a parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParameterResult) -> dict:
    out: dict = {}
    if "parameter" in value:
        import aws_sdk_ssm.types.parameter

        out["Parameter"] = aws_sdk_ssm.types.parameter.serialize_aws_json_1_1(
            value["parameter"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParameterResult:
    out: GetParameterResult = {}  # type: ignore[typeddict-item]
    if "Parameter" in data:
        import aws_sdk_ssm.types.parameter

        out["parameter"] = aws_sdk_ssm.types.parameter.deserialize_aws_json_1_1(
            data["Parameter"]
        )
    return out
