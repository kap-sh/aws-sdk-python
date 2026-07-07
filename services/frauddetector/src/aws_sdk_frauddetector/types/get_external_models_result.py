"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetExternalModelsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.external_model_list
    import aws_sdk_frauddetector.types.string


class GetExternalModelsResult(TypedDict, closed=True):
    external_models: NotRequired[
        "aws_sdk_frauddetector.types.external_model_list.ExternalModelList"
    ]
    """<p>Gets the Amazon SageMaker models.</p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next page token to be used in subsequent requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExternalModelsResult) -> dict:
    out: dict = {}
    if "external_models" in value:
        import aws_sdk_frauddetector.types.external_model_list

        out["externalModels"] = (
            aws_sdk_frauddetector.types.external_model_list.serialize_aws_json_1_1(
                value["external_models"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExternalModelsResult:
    out: GetExternalModelsResult = {}  # type: ignore[typeddict-item]
    if "externalModels" in data:
        import aws_sdk_frauddetector.types.external_model_list

        out["external_models"] = (
            aws_sdk_frauddetector.types.external_model_list.deserialize_aws_json_1_1(
                data["externalModels"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
