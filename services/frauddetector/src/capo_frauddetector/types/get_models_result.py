"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetModelsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.model_list
    import capo_frauddetector.types.string


class GetModelsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next page token to be used in subsequent requests.</p>"""
    models: NotRequired["capo_frauddetector.types.model_list.modelList"]
    """<p>The array of models.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetModelsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "models" in value:
        import capo_frauddetector.types.model_list

        out["models"] = capo_frauddetector.types.model_list.serialize_aws_json_1_1(
            value["models"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetModelsResult:
    out: GetModelsResult = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "models" in data:
        import capo_frauddetector.types.model_list

        out["models"] = capo_frauddetector.types.model_list.deserialize_aws_json_1_1(
            data["models"]
        )
    return out
