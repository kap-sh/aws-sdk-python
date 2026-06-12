"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetModelsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.model_list
    import aws_sdk_frauddetector.types.string


class GetModelsResult(TypedDict):
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next page token to be used in subsequent requests.</p>"""
    models: NotRequired["aws_sdk_frauddetector.types.model_list.modelList"]
    """<p>The array of models.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetModelsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "models" in value:
        import aws_sdk_frauddetector.types.model_list

        out["models"] = aws_sdk_frauddetector.types.model_list.serialize_aws_json_1_1(
            value["models"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetModelsResult:
    out: GetModelsResult = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "models" in data:
        import aws_sdk_frauddetector.types.model_list

        out["models"] = aws_sdk_frauddetector.types.model_list.deserialize_aws_json_1_1(
            data["models"]
        )
    return out
