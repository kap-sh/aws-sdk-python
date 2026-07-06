"""Generated from Smithy shape ``com.amazonaws.connect#CreateUseCaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.use_case_id


class CreateUseCaseResponse(TypedDict, closed=True):
    use_case_id: NotRequired["aws_sdk_connect.types.use_case_id.UseCaseId"]
    """<p>The identifier of the use case.</p>"""
    use_case_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the use case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUseCaseResponse) -> dict:
    out: dict = {}
    if "use_case_id" in value:
        out["UseCaseId"] = value["use_case_id"]
    if "use_case_arn" in value:
        out["UseCaseArn"] = value["use_case_arn"]
    return out


def deserialize_json(data: dict) -> CreateUseCaseResponse:
    out: CreateUseCaseResponse = {}  # type: ignore[typeddict-item]
    if "UseCaseId" in data:
        out["use_case_id"] = data["UseCaseId"]
    if "UseCaseArn" in data:
        out["use_case_arn"] = data["UseCaseArn"]
    return out
