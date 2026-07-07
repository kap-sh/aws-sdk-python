"""Generated from Smithy shape ``com.amazonaws.connect#UseCase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.use_case_id
    import aws_sdk_connect.types.use_case_type


class UseCase(TypedDict, closed=True):
    use_case_id: NotRequired["aws_sdk_connect.types.use_case_id.UseCaseId"]
    """<p>The identifier for the use case.</p>"""
    use_case_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the use case.</p>"""
    use_case_type: NotRequired["aws_sdk_connect.types.use_case_type.UseCaseType"]
    """<p>The type of use case to associate to the integration association. Each integration association can have only one of each use case type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UseCase) -> dict:
    out: dict = {}
    if "use_case_id" in value:
        out["UseCaseId"] = value["use_case_id"]
    if "use_case_arn" in value:
        out["UseCaseArn"] = value["use_case_arn"]
    if "use_case_type" in value:
        import aws_sdk_connect.types.use_case_type

        out["UseCaseType"] = aws_sdk_connect.types.use_case_type.serialize_json(
            value["use_case_type"]
        )
    return out


def deserialize_json(data: dict) -> UseCase:
    out: UseCase = {}  # type: ignore[typeddict-item]
    if "UseCaseId" in data:
        out["use_case_id"] = data["UseCaseId"]
    if "UseCaseArn" in data:
        out["use_case_arn"] = data["UseCaseArn"]
    if "UseCaseType" in data:
        import aws_sdk_connect.types.use_case_type

        out["use_case_type"] = aws_sdk_connect.types.use_case_type.deserialize_json(
            data["UseCaseType"]
        )
    return out
